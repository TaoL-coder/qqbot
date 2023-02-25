from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command,on_natural_language
from services.common import ServiceException
from aiocqhttp.message import MessageSegment
# ... 略
from services.btc import get_btc,get_zy_btc,check_account
from services.btc import create_account,dealing,get_setu


from nonebot.natural_language import NLPSession, IntentCommand

__plugin_name__ = 'btc'
__plugin_usage__ = '用法： 对我说 "btc价格"，我会回复 "btc价格!"'

btc_permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser



__plugin_name__ = '色图'
__plugin_usage__ = '用法： ’对我‘说 "色图"，我会回复色图'


@on_natural_language(keywords={'色图','涩图', 'setu'},permission=btc_permission,only_to_me=False)
async def _(session: CommandSession):
    return IntentCommand(60, '色图')
    
@on_command('色图', aliases=('涩图', 'setu'),permission=btc_permission)
async def _(session: CommandSession):
    ses = str(session.event.message)
    im_b64 = get_setu(ses)
    await session.send(MessageSegment.image(f'base64://{im_b64}'))
    

'''@on_command('色图', aliases=('涩图', 'setu'),permission=btc_permission)
async def _(session: CommandSession):
    im_b64 = get_setu()
    await session.send(MessageSegment.image(f'base64://{im_b64}'))'''



@on_command('btc价格', aliases=('比特币价格', 'BTC价格','btc现在价格','BTC现在价格','比特币现在价格'),permission=btc_permission)
async def _(session: CommandSession):
    result = 'BTC现在价格为：{:.2f}'.format(get_btc())
    await session.send(result,at_sender=True)
    
    
 
__plugin_name__ = 'btc周线'
__plugin_usage__ = '用法： 对我说 "btc周线"，我会回复 "btc周线图片!"'


@on_command('btc周线', aliases=('比特币周线', 'BTC周线'),permission=btc_permission)
async def _(session: CommandSession):
    im_b64 = get_zy_btc(zy='z')
    await session.send(MessageSegment.image(f'base64://{im_b64}'), at_sender=True)
    
    
    
__plugin_name__ = 'btc日线'
__plugin_usage__ = '用法： 对我说 "btc日线"，我会回复 "btc日线图片!"'


@on_command('btc日线', aliases=('比特币日线', 'BTC日线'),permission=btc_permission)
async def _(session: CommandSession):
    im_b64 = get_zy_btc(zy='r')
    await session.send(MessageSegment.image(f'base64://{im_b64}'), at_sender=True)
    
    
    
    
    
__plugin_name__ = 'btc15分线'
__plugin_usage__ = '用法： 对我说 "btc15分线"，我会回复 "btc15分图片!"'


@on_command('btc15分时线', aliases=('比特币15分线','比特币15分时线','btc15分线','BTC15分线','BTC15分时线'),permission=btc_permission)
async def _(session: CommandSession):
    im_b64 = get_zy_btc(zy='f')
    await session.send(MessageSegment.image(f'base64://{im_b64}'), at_sender=True)
    
    
    
    
__plugin_name__ = '创建账号'
__plugin_usage__ = '用法： 对我说 "创建账号"，我会回复 "创建成功，账户余额：一个小目标!"'


@on_command('创建账号', aliases=('创建账户'),permission=btc_permission)
async def _(session: CommandSession):
    user_id, group_id = session.event.user_id, session.event.group_id
    result = create_account(user_id)
    await session.send(result, at_sender=True)
    
    
    
__plugin_name__ = '账号余额'
__plugin_usage__ = '用法： 对我说 "账号余额"，我会回复 "账户余额"'


@on_command('账号查询', aliases=('账户余额查询','账户余额','账号余额查询','账户查询','余额查询'),permission=btc_permission)
async def _(session: CommandSession):
    user_id, group_id = session.event.user_id, session.event.group_id
    result = ''.join(['\n账户余额为:%.2f' % check_account(user_id)[0],'\n持有BTC:%.2f'%check_account(user_id)[2]])
    await session.send(result, at_sender=True)
    
 
 
 
__plugin_name__ = '交易btc'
__plugin_usage__ = '用法： 对我说 "交易btc"，我会回复 "交易"'


@on_command('交易btc', aliases=('交易BTC', '交易比特币','交易'), permission=btc_permission)
async def _(session: CommandSession):
    # 若用户对机器人说“天气”，则此变量为 `['']`
    # 若用户对机器人说“天气 香港”，则此变量为 `['香港']`
    # 若用户对机器人说“天气 香港 详细”，则此变量为 `['香港', '详细']`
    args = session.current_arg_text.strip().split(' ', 1)

    if not args[0]:  #没有买入卖出
        bos = await session.aget(key='买入或卖出', prompt='请问是买入还是卖出呢？', at_sender=True)
    else:
        bos = args[0]  #附带了买入卖出  bos只能是买入或者卖出可附带金额或加百分比

    try:
        user_id = session.event.user_id
        result = dealing(bos,user_id)
    except ServiceException as e:
        result = e.message

    await session.send(result)
    

    
    
    
    
    