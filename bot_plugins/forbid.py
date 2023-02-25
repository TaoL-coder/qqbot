import nonebot
from nonebot.command import CommandSession
import os

from services.forbid import check_sign,recog_pic


bot = nonebot.get_bot()


__plugin_name__ = '禁言'
__plugin_usage__ = '当收到群弟弟发叔叔时，禁言臭弟弟'

check_permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser

bot = nonebot.get_bot()



@bot.on_message('group')
async def _(session):    #<Event, {'anonymous': None, 'font': 0, 'group_id': 372847571, 'message': [{'type': 'image', 'data': {'file': '56a57191b3c1862a7a74d8fe69fd91f7.image', 'url': 'https://gchat.qpic.cn/gchatpic_new/781279348/2637847571-2949991389-56A57191B3C1862A7A74D8FE69FD91F7/0?term=3'}}], 'message_id': -656576355, 'message_seq': 4518, 'message_type': 'group', 'post_type': 'message', 'raw_message': '[CQ:image,file=56a57191b3c1862a7a74d8fe69fd91f7.image]', 'self_id': 1146531857, 'sender': {'age': 0, 'area': '', 'card': '', 'level': '', 'nickname': 'today is a beautiful day', 'role': 'owner', 'sex': 'unknown', 'title': '', 'user_id': 781279348}, 'sub_type': 'normal', 'time': 1627834568, 'user_id': 781279348}>
    group_list = [161227259,665034936] #群列表
    dd_list = [2240150297,562304461] #弟弟名单
    gg_list = [122462994]
    words = ['叔','shu','大伯']
    count = 0
    gg_count = 0
    if session.group_id in group_list and session.user_id in dd_list:
        ssm = str(session.message)
        if 'CQ:image' in ssm:
            check_sign(session=ssm)
            result = recog_pic()
            for line in result:
                for j in words:
                    if j in line[1][0]:
                        count += 1
                        break
        else:  
            for i in words:
                if i in ssm:
                    count += 1
                    break
    if session.group_id in gg_list: 
        ssm = str(session.message)
        if '发财' in ssm:
            gg_count += 1
            
    if count > 0:
        await bot.send_group_msg(group_id=session.group_id, message="网络不是无法之地，平安中国慎言慎行！！")
        num = os.listdir('/home/luo/my_bot/799/pic_db/time/')[0]
        time = int(num)
        await bot.set_group_ban(user_id=session.user_id,group_id=session.group_id,duration = time*60)
        os.rename('/home/luo/my_bot/799/pic_db/time/'+num,'/home/luo/my_bot/799/pic_db/time/'+str((time+5)))
    if gg_count > 0: 
        await bot.send_group_msg(group_id=session.group_id, message="请安静一下，今天吃面哦！！")
        await bot.set_group_ban(user_id=session.user_id,group_id=session.group_id,duration = 5*60)


