
'''
from services.jd_info import get_jd
from aiocqhttp.message import MessageSegment
import nonebot






@nonebot.scheduler.scheduled_job('cron', hour='21')
async def _():
    bot = nonebot.get_bot()
    result_list = get_jd()
    for i in result_list:
        await bot.send_group_msg(group_id=372847571,message=i)
        #test 665034936
        #能量 372847571'''
    