import matplotlib.pyplot as plt
import os,re,time,random,requests,datetime
from retrying import retry
from io import BytesIO  # 新
from base64 import b64encode  # 新
from PIL import Image
from numpy import argmin,argmax
from json import loads,dump,load

import urllib.request as ur

USER_AGENTS = [
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1"
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
        "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12 "
        ]

def url_open(url):
    headers = {}
    headers['User-Agent'] = random.choice(USER_AGENTS)
    ret = requests.get(url,headers=headers,timeout=30)
    html = ret.content.decode('utf-8') #隐藏
    return html
  
def url_open2(url):
    headers = {}
    headers['User-Agent'] = random.choice(USER_AGENTS)
    ret = ur.Request(url,headers=headers)
    response = ur.urlopen(ret)
    html = response.read() #隐藏
    return html
    
def get_setu(session):
    image = Image.open('/home/luo/my_bot/799/pic_db/setu.jpg')
    buff = BytesIO()
    image.save(buff, 'jpeg')
    return b64encode(buff.getvalue()).decode()
    
    #换一下注释就能用
    '''tag = []
    if '白丝' in session:
        tag.append('白丝')
    if '黑丝' in session:
        tag.append('黑丝')
    if '二次元' in session:
        tag.append('二次元')
    if '少女' in session:
        tag.append('少女')
    if '萝莉' in session:
        tag.append('萝莉')
    if '裸足' in session:
        tag.append('裸足')
    if 'KR' in session or 'kr' in session or 'Kr' in session:
        tag = None
    if tag == None:
        image = Image.open(f'/home/luo/my_bot/799/pic_db/st/kr{random.randint(1,2)}.jpg')
        buff = BytesIO()
        image.save(buff, 'jpeg')
        return b64encode(buff.getvalue()).decode()
    else:
        str_tar = '&'.join(tag)
        uo = url_open(f'https://api.lolicon.app/setu/v2?tag={str_tar}')
        dict_api = loads(uo)
        img_url = dict_api['data'][0]['urls']['original'].replace('original','master').replace('.jpg','_master1200.jpg').replace('.png','_master1200.png')
        print(img_url)
        img = url_open2(img_url)
        try:
            os.system('rm /home/luo/my_bot/799/pic_db/st/st.jpg')
        except:
            pass
        with open('/home/luo/my_bot/799/pic_db/st/st.jpg','ab') as f0:
            f0.write(img)
        image = Image.open('/home/luo/my_bot/799/pic_db/st/st.jpg')
        buff = BytesIO()
        image.save(buff, 'jpeg')
        return b64encode(buff.getvalue()).decode()'''
        
def get_zy_btc(zy='z'): 
    zhou_list_col = []
    zhou_list_row = []
    f_step = 1
    if zy == 'r':
        html = url_open('https://api.btcfans.com/api/price/get-coin-ticker-history?code=bitcoin&end=16290848000&granularity=86400&size=20')
        step = 1
        date_count = 20
    elif zy == 'z':
        html = url_open('https://api.btcfans.com/api/price/get-coin-ticker-history?code=bitcoin&end=16290848000&granularity=604800&size=20')
        step = 7
        date_count = 140
    elif zy == 'f':
        html = url_open('https://api.btcfans.com/api/price/get-coin-ticker-history?code=bitcoin&end=16290848000&granularity=900&size=20')
        step = 15
        date_count = 300
        
    for i in loads(html)['Data']:
        zhou_list_col.append(i[1])
    zhou_list_col = zhou_list_col[::-1]  
    
    d = datetime.datetime.now()
    
    for i in range(0,date_count,step):  #(0,7)表示截取今天到七天前的日期，昨天到七天前的日期用（1,8）
        if zy=='f':
            date= ((d-datetime.timedelta(minutes=i)).strftime("%Y-%m-%d %H:%M:%S"))
            minue= date[11:16]
            zhou_list_row.append(minue)
        else:
            oneday = datetime.timedelta(days=i)
            day = d - oneday
            date_to = datetime.datetime(day.year, day.month, day.day)
            zhou_list_row.append(str(date_to)[5:10])  #[：10]表示展示的是年月日，若是要展示月日用[5：10],若是要展示年月日时分秒用[：]
    zhou_list_row = zhou_list_row[::-1]
    
    plt.figure(figsize=(15, 5))
    y1_min=argmin(zhou_list_col)
    y1_max=argmax(zhou_list_col)
    show_min=' '+str(zhou_list_col[y1_min])
    show_max=' '+str(zhou_list_col[y1_max])
    # 以●绘制最大值点和最小值点的位置
    plt.plot(y1_min,zhou_list_col[y1_min],'ko') 
    plt.plot(y1_max,zhou_list_col[y1_max],'ko')
    plt.annotate(show_min,xy=(y1_min,zhou_list_col[y1_min]),xytext=(y1_min,zhou_list_col[y1_min]))
    plt.annotate(show_max,xy=(y1_max,zhou_list_col[y1_max]),xytext=(y1_max,zhou_list_col[y1_max]))
    plt.plot(zhou_list_row,zhou_list_col)
    plt.title('Bitcoin_week')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.savefig('/home/luo/my_bot/799/pic_db/zy.jpg')
    image = Image.open('/home/luo/my_bot/799/pic_db/zy.jpg')
    buff = BytesIO()
    image.save(buff, 'jpeg')
    return b64encode(buff.getvalue()).decode()

  

def get_btc():
    html = url_open('https://api.btcfans.com/api/price/get-coin-ticker-history?code=bitcoin&end=16290848000&granularity=86400&size=1')
    return loads(html)['Data'][0][1]
    
    
    
def create_account(user_id):
    db = '/home/luo/my_bot/799/pic_db/account.json'
    with open(db) as f:
        dict_ = load(f)
    
    if str(user_id) in dict_:
        return '账户已存在!不要再尝试啦~~'
    else:
        with open(db,'w') as f:
            dict_[str(user_id)] = [1000000,{'record':[]},0]
            dump(dict_,f)
            return '创建成功，账户余额：1000000'
            
def check_account(user_id):
    db = '/home/luo/my_bot/799/pic_db/account.json'
    with open(db) as f:
        dict_ = load(f)
        hold = dict_[str(user_id)][2]
        btc_price = int(get_btc())
        count = hold*btc_price
        return (dict_[str(user_id)][0],dict_,count)
 

    

 
def dealing(bos:str,user_id):
    db = '/home/luo/my_bot/799/pic_db/account.json'
    btc_price = int(get_btc())
    balance = check_account(user_id)[0]
    hold_bal = check_account(user_id)[2]
    dict_ = check_account(user_id)[1]
    now_time = str(datetime.datetime.now())[:16]
    _dig = int(re.findall('\d+',bos)[0])
    if r'%' in bos:
        if '买入' in bos:
            if 0<=_dig<=100:
                new_dig = _dig/100*balance
            else:
                new_dig = 0
        elif '卖出' in bos:
            if 0<=_dig<=100:
                new_dig = _dig/100*hold_bal
            else:
                new_dig = 0
    else:
        new_dig = _dig

    if '买入' in bos:
        if new_dig > balance:
            return '账户余额不足！！'
        else:
            dict_[str(user_id)][1]['record'].append([now_time,'Buy',new_dig])
            dict_[str(user_id)][0] = balance - new_dig
            dict_[str(user_id)][2] += new_dig/btc_price
            with open(db,'w') as f:
                dump(dict_,f)
            hold_bal_new = check_account(user_id)[2]
            return '买入成功,账户余额为:{:.2f},持有BTC{:.2f}'.format(dict_[str(user_id)][0],hold_bal_new)
            
    elif new_dig == 0:
        return '无法交易0%或者超过100%的BTC'
        
    elif '卖出' in bos:
        if hold_bal < new_dig:
            return '你卖个锤子卖，都没有持有那么多！'
        else:
            dict_[str(user_id)][1]['record'].append([now_time,'Sell',new_dig])
            dict_[str(user_id)][0] = balance + new_dig
            dict_[str(user_id)][2] -= new_dig/btc_price
            with open(db,'w') as f:
                dump(dict_,f)
            hold_bal_new = check_account(user_id)[2]
            return '卖出成功,账户余额为:{:.2f},持有BTC{:.2f}'.format(dict_[str(user_id)][0],hold_bal_new)
    
    
            
            
            
            
            
            
            
            
            
            
