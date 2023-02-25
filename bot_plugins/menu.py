from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command







_permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser



__plugin_name__ = '菜单'
__plugin_usage__ = '用法： ’对我‘说 "菜单"，回复各种功能'

@on_command('菜单',aliases=('帮助','功能'),permission=_permission)
async def _(session: CommandSession):
    line1 = '菜单命令:\n'
    line2 = '历史今日\n狗屁不通\n'
    results = line1+line2
    await session.send(message = results)