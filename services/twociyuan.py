import os,time,random,requests,json,re
from retrying import retry
from io import BytesIO  # 新
from base64 import b64encode  # 新
from PIL import Image


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
    
    
def get_ecy():
    url = 'https://api.iyk0.com/ecy/api.php'
    pic = url_open2(url)
    pic_path = '/home/luo/my_bot/799/pic_db/erciyuan.jpg'
    try:
        os.system(f'rm {pic_path}')
    except:
        pass
    with open(pic_path,'ab') as f0:
        f0.write(pic)
    image = Image.open(pic_path)
    buff = BytesIO()
    image.save(buff, 'jpeg')
    return b64encode(buff.getvalue()).decode()
    
    
    
    
def gpbt(word):
    count = int(re.findall('\d+',word)[0])
    if count>800:
        count = 800
    words = word.replace(re.findall('\d+',word)[0],'')
    new_words = str(words.encode('utf-8')).upper().replace('\X',"\%").replace('\\','')[2:-1]
    url = f'https://api.iyk0.com/gpbt/?msg={new_words}&num={count}'
    data = json.loads(url_open2(url))["data"]
    return data
   
    
    
def goodmorning():
    pic_path = '/home/luo/my_bot/799/pic_db/moring.jpg'
    image = Image.open(pic_path)
    buff = BytesIO()
    image.save(buff, 'jpeg')
    return b64encode(buff.getvalue()).decode()
    
    
def meitui():
    pic_path = '/home/luo/my_bot/799/pic_db/meitui.jpg'
    url = 'https://api.iyk0.com/mtt'
    pic = url_open2(url)
    try:
        os.system(f'rm {pic_path}')
    except:
        pass
    with open(pic_path,'ab') as f0:
        f0.write(pic)
    image = Image.open(pic_path)
    buff = BytesIO()
    image.save(buff, 'jpeg')
    return b64encode(buff.getvalue()).decode()
