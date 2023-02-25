from services.twociyuan import get_ecy,gpbt,goodmorning,meitui
from aiocqhttp.message import MessageSegment
import nonebot
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command,on_natural_language
from nonebot.natural_language import NLPSession, IntentCommand
from services.common import ServiceException
from nonebot.helpers import send
import random,re


bot = nonebot.get_bot()

_permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser


__plugin_name__ = '二次元'
__plugin_usage__ = '用法： ’对我‘说 "二次元"，我会回复二次元图片'



@on_natural_language(keywords={'二次元','来点二次元图片', '搞点二次元图片'},permission=_permission,only_to_me=False)
async def _(session: CommandSession):
    return IntentCommand(60, '二次元')
    
@on_command('二次元',permission=_permission)
async def _(session: CommandSession):
    im_b64 = get_ecy()
    await session.send(MessageSegment.image(f'base64://{im_b64}'))
    
    

__plugin_name__ = '狗屁不通'
__plugin_usage__ = '用法： ’对我‘说 "狗屁不通"，我会回复文字'


@on_command('狗屁不通', aliases=('狗屁不通文章生成', '狗屁不通文字生成'), permission=_permission)
async def _(session: CommandSession):
    # 若用户对机器人说“天气”，则此变量为 `['']`
    # 若用户对机器人说“天气 香港”，则此变量为 `['香港']`
    # 若用户对机器人说“天气 香港 详细”，则此变量为 `['香港', '详细']`
    
    word = await session.aget(key='买入或卖出', prompt='请输入关键词与字数，\n如:笨笨发财800', at_sender=True)
    
    try:
        result = gpbt(word=word)
    except ServiceException as e:
        result = e.message

    await session.send(result,at_sender=True)
    
    
#复读机

__plugin_name__ = '复读'
__plugin_usage__ = '自动复读'


'''@on_natural_language(keywords={'发财'},permission=_permission,only_to_me=False)
async def _(session: CommandSession):
    return IntentCommand(60, '发财n')
    
@on_command('发财n',permission=_permission)
async def _(session: CommandSession):
    #665034936 测试
    #122462994 基金
    rr = random.randint(1,10)
    if rr>5:
        if session.event.group_id == 665034936:
            res = str(session.event.message)
            await session.send(res)'''
        
@bot.on_message('group')
async def _(session):    #<Event, {'anonymous': None, 'font': 0, 'group_id': 372847571, 'message': [{'type': 'image', 'data': {'file': '56a57191b3c1862a7a74d8fe69fd91f7.image', 'url': 'https://gchat.qpic.cn/gchatpic_new/781279348/2637847571-2949991389-56A57191B3C1862A7A74D8FE69FD91F7/0?term=3'}}], 'message_id': -656576355, 'message_seq': 4518, 'message_type': 'group', 'post_type': 'message', 'raw_message': '[CQ:image,file=56a57191b3c1862a7a74d8fe69fd91f7.image]', 'self_id': 1146531857, 'sender': {'age': 0, 'area': '', 'card': '', 'level': '', 'nickname': 'today is a beautiful day', 'role': 'owner', 'sex': 'unknown', 'title': '', 'user_id': 781279348}, 'sub_type': 'normal', 'time': 1627834568, 'user_id': 781279348}>
    group_list = [122462994,161227259,665034936]
    norept_list = [1097774129]
    if session.group_id in group_list and session.user_id not in norept_list:
        ssm = str(session.message)
        if ('早' == ssm) or ('早安' in ssm) or ('早上好' in ssm):
            mes  = '''[CQ:image,file=179fd1cda108ebbb8760644f5c567fdf.image,url=https://gchat.qpic.cn/gchatpic_new/781279348/665034936-3084182491-179FD1CDA108EBBB8760644F5C567FDF/0?term=3,subType=0][CQ:xml,data=<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="5" templateID="1" action="" brief="&#91;图片表情&#93;" sourceMsgId="0" url="" flag="0" adverSign="0" multiMsgFlag="0"><item layout="0" advertiser_id="0" aid="0"><image uuid="179FD1CDA108EBBB8760644F5C567FDF.jpg" md5="179FD1CDA108EBBB8760644F5C567FDF" GroupFiledid="3084182491" filesize="7635" local_path="/storage/emulated/0/Android/data/com.tencent.mobileqq/Tencent/MobileQQ/chatpic/chatimg/3b5/Cache_17cadcd6a11a53b5" minWidth="400" minHeight="400" maxWidth="400" maxHeight="400" /></item><source name="" icon="" action="" appid="-1" /></msg>,resid=60]'''
            await send(bot = bot, message = mes, event = {'group_id':session.group_id})
        ssm = str(session.message)
        rr = random.randint(1,15)
        if rr>14:
            await send(bot=bot,message=ssm,event = {'group_id':session.group_id})
            
    
    

__plugin_name__ = '来点美腿'
__plugin_usage__ = '用法： ’对我‘说 "美腿"，我会回复美腿图片'


    
@on_command('美腿',permission=_permission)
async def _(session: CommandSession):
    im_b64 = meitui()
    await session.send(MessageSegment.image(f'base64://{im_b64}'))
    
    
__plugin_name__ = '四六级'
__plugin_usage__ = '用法： ’对我‘说 "四六级"，我会回复二次元图片'


    
@on_command('四六级',permission=_permission)
async def _(session: CommandSession):
    ssm = '四六级报名、打印准考证页面	http://cet-bm.neea.edu.cn/'
    await session.send(ssm)
    

__plugin_name__ = '表情包放大'
__plugin_usage__ = '用法： ’对我‘说 "表情包放大"，我会回复放大的表情包'


    
@on_command('表情包放大',permission=_permission)
async def _(session: CommandSession):
    meme = await session.aget(key='nan', prompt='请发送表情包', at_sender=True)
    if meme[:9] == '[CQ:image':
        uuid = re.findall('file=(.+?).image',meme)[0].upper()
        bigger = f'''[CQ:xml,data=<?xml version=\'1.0\' encoding=\'UTF-8\' standalone=\'yes\' ?><msg serviceID="5" templateID="1" action="" brief="&#91;图片表情&#93;" sourceMsgId="0" url="" flag="0" adverSign="0" multiMsgFlag="0"><item layout="0" advertiser_id="0" aid="0"><image uuid="{uuid}.jpg" md5="{uuid}" GroupFiledid="2747963108" filesize="35691" local_path="" minWidth="400" minHeight="400" maxWidth="400" maxHeight="400" /></item><source name="" icon="" action="" appid="-1" /></msg>,resid=60]'''
        print('this is  ',meme+bigger)
        await session.send(meme+bigger)
    else:
        rr = random.randint(1,20)
        if rr>19:
            resu = 'wdnmd，说了发图片不听是吧！！'
        else:
            resu = '您发的不是图片，酒酒解析不出来哦~'
        await session.send(resu)
    
    
    
    
    
#de5bcad1525fb5014f2714defccbabfb.image
#<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><msg serviceID="5" templateID="1" action="" brief="[图片表情]" sourceMsgId="0" url="" flag="0" adverSign="0" multiMsgFlag="0"><item layout="0" advertiser_id="0" aid="0"><image uuid="de5bcad1525fb5014f2714defccbabfb.image" md5="6CCBDE7E8E2D91011CB3DAF1C45BB99F" GroupFiledid="0" filesize="2964" local_path="" minWidth="400" minHeight="400" maxWidth="400" maxHeight="400" /></item><source name="" icon="" action="" appid="-1" /></msg>
    
    
    
    
    
    