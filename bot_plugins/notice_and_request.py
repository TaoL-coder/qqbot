from nonebot import on_notice, NoticeSession

# 将函数注册为群成员增加通知处理器
@on_notice('group_increase')
async def _(session: NoticeSession):
    if session.event.group_id == 161227259:
        # 发送欢迎消息
        await session.send('欢迎报考生物工程！！我是本群的机器人~,有什么事可以问别人', at_sender=True)