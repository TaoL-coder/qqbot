from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from nonebot.natural_language import NLPSession, IntentCommand
from services.common import ServiceException
from services.today_history import get_history







_permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser



__plugin_name__ = '历史今天'
__plugin_usage__ = '用法： ’对我‘说 "历史今天"，历史上的今天'

@on_command('历史今天',aliases=('历史今日','那年今日'),permission=_permission)
async def _(session: CommandSession):
    await session.send(message = get_history())
    
    