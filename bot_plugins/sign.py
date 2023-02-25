from nonebot.command import CommandSession
from services.common import ServiceException
from aiocqhttp.message import MessageSegment
from nonebot.experimental.plugin import on_natural_language,on_command
from nonebot.natural_language import NLPSession, IntentCommand
import nonebot

from services.sign import check_sign,recog_pic,create_subscriber,del_subscriber
from nonebot.helpers import send

import requests

__plugin_name__ = '签到'
__plugin_usage__ = '当受到某个群里的图片后，提取文字识别名字，后转告未签到者'

#check_permission = lambda sender: sender.is_privatechat or sender.is_superuser

bot = nonebot.get_bot()


# 只要消息包含“CQ:image”，就执行此处理器
@bot.on_message('group')
async def _(session):    #<Event, {'anonymous': None, 'font': 0, 'group_id': 372847571, 'message': [{'type': 'image', 'data': {'file': '56a57191b3c1862a7a74d8fe69fd91f7.image', 'url': 'https://gchat.qpic.cn/gchatpic_new/781279348/2637847571-2949991389-56A57191B3C1862A7A74D8FE69FD91F7/0?term=3'}}], 'message_id': -656576355, 'message_seq': 4518, 'message_type': 'group', 'post_type': 'message', 'raw_message': '[CQ:image,file=56a57191b3c1862a7a74d8fe69fd91f7.image]', 'self_id': 1146531857, 'sender': {'age': 0, 'area': '', 'card': '', 'level': '', 'nickname': 'today is a beautiful day', 'role': 'owner', 'sex': 'unknown', 'title': '', 'user_id': 781279348}, 'sub_type': 'normal', 'time': 1627834568, 'user_id': 781279348}>
    if (session.user_id == 781279348 and session.group_id == 665034936) or session.user_id == 108272496:
        ssm = str(session.message)
        if 'CQ:image' in ssm:
            check_sign(session=ssm)
            tx_list = recog_pic()


            #微信config
            title = '**今日校园打卡提醒**'
            msg = '![QQ图片20211021153929.jpg](https://i.loli.net/2021/10/21/Bp6M89ts1O4JW2E.jpg)'
            
            data = {"key":"value"}
            #res = requests.post(url=url,data=data)
            #print(res.text)
            
            for i in tx_list:
                print(len(tx_list))
                await send(bot=bot,message='今日校园打卡啦~', event = {'user_id':int(i[0])})
                                
                #微信
                try:
                    sendkey = i[1]
                    url = f"https://sctapi.ftqq.com/{sendkey}.send?title={title}&desp={msg}"
                    await requests.post(url=url,data=data)
                except:
                    print(requests.post(url=url,data=data))
                    pass
            '''for i in jg_list:
                await send(bot=bot,message=f'{i}置信度不高，你看看', event = {'user_id':781279348})
            for i in tx_list:
                await send(bot=bot,message='打卡啦~', event = {'user_id':int(i),'group_id': 372847571},at_sender=True)'''
            #send(bot, event, message, *, ensure_private=False, ignore_failure=True, **kwargs)

    

@on_command('订阅打卡', aliases=('打卡订阅'))
async def _(session: CommandSession):
    name = await session.aget(key='name', prompt='请问您的姓名是？', at_sender=True)
    sendkey = await session.aget(key='sendkey', prompt='姓名获取成功！如果要获取微信推送，请访问https://sct.ftqq.com/login，根据提示微信扫码登陆后，将sendkey发送给我~\n若不需要微信推送，可任意回复结束此次会话，依然保存QQ私聊打卡提醒~', at_sender=True)
    try:
        user_id = session.event.user_id
        result = create_subscriber(name=name,user_id=user_id,sendkey=sendkey)
        
    except ServiceException as e:
        result = e.message
        
    await session.send(result, at_sender=True)
    

@on_command('取消订阅', aliases=('关闭订阅'))
async def _(session: CommandSession):
    user_id = session.event.user_id
    result = del_subscriber(user_id)
    await session.send(result, at_sender=True)
    
    

