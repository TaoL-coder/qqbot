from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from services.scheduler import get_weather,sixths,getthswp,getthswp
from aiocqhttp.message import MessageSegment



@nonebot.scheduler.scheduled_job('cron', hour='09')
async def _():
    bot = nonebot.get_bot()
    result = get_weather()
    im_b64 = sixths()
    try:
        message=result+MessageSegment.image(f'base64://{im_b64}')
        await bot.send_group_msg(group_id=122462994,message=message)
    except CQHttpError:
        pass
  
 
'''@nonebot.scheduler.scheduled_job('cron', hour='11',minute='40')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    result = '截止上午收盘，板块热度：'
    im_b64 = getthswp()
    try:
        message=result+MessageSegment.image(f'base64://{im_b64}')
        await bot.send_group_msg(group_id=122462994,message=message)
    except CQHttpError:
        pass       
 #665034936
 

@nonebot.scheduler.scheduled_job('cron', hour='15',minute='10') 
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    result = '截止3点收盘，板块热度：'
    im_b64 = getthswp()
    try:
        message=result+MessageSegment.image(f'base64://{im_b64}')
        await bot.send_group_msg(group_id=122462994,message=message)
    except CQHttpError:
        pass''' 
        
        
'''(year=None, month=None, day=None, week=None, day_of_week=None, hour=None, minute=None, second=None, start_date=None, end_date=None, timezone=None, jitter=None)
Parameters
year (int|str) – 4-digit year

month (int|str) – month (1-12)

day (int|str) – day of month (1-31)

week (int|str) – ISO week (1-53)

day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)

hour (int|str) – hour (0-23)

minute (int|str) – minute (0-59)

second (int|str) – second (0-59)

start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)

end_date (datetime|str) – latest possible date/time to trigger on (inclusive)

timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)

jitter (int|None) – delay the job execution by jitter seconds at most'''