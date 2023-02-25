import requests,random,json,os,re
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
    ret = requests.get(url,headers=headers,timeout=60)
    html = ret.content.decode('utf-8') #隐藏
    return html

def url_open2(url):
    headers = {}
    headers['User-Agent'] = random.choice(USER_AGENTS)
    ret = ur.Request(url,headers=headers)
    response = ur.urlopen(ret)
    html = response.read() #隐藏
    return html   
    
def get_weather():
    try:
        wea = url_open('https://api.iyk0.com/3rtq/?msg=%E5%8E%A6%E9%97%A8&b=6')
        today = '\n'.join(wea.split('\n')[8:12])
        tomarrow = '\n'.join(wea.split('\n')[14:18])
        result = f'继续亏钱!!!\n昨日旧闻：\n'
        return result
    except:
        result = f'继续亏钱!!!\n昨日旧闻：\n'
        return result
    
    
def sixths():
    url = 'https://api.iyk0.com/60s/'
    img_url = json.loads(url_open(url))['imageUrl']
    img = url_open2(img_url)
    pic_path = '/home/luo/my_bot/799/pic_db/60s.jpg'
    try:        
        os.system(f'rm {pic_path}')
    except:
        pass
    with open(pic_path,'ab') as f0:
        f0.write(img)
    image = Image.open(pic_path)
    buff = BytesIO()
    image = image.convert('RGB')
    image.save(buff, 'jpeg')
    return b64encode(buff.getvalue()).decode()
    
    
   
    
def url_open3(url):  #加了cookie的
    headers = {}
    headers['User-Agent'] = random.choice(USER_AGENTS)
    headers['Cookie'] = 'v=A9pXDbjdb85ewONidLAEjjzNK4v_C17l0I_SieRThm04V3A9zJuu9aAfIpi3'
    headers['Accept'] ='text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    ret = ur.Request(url,headers=headers)
    response = ur.urlopen(ret)
    html = response.read() #隐藏
    return html
    
 
def getthswp():
    url = 'https://ai.iwencai.com/searchapi?q=A%E8%82%A1%E5%8D%88%E8%AF%84&tid=info&p=1&jump=0' #午评
    url_picin = json.loads(url_open3(url))['data']['list'][0]['list'][0]['URL']
    allhtml = str(url_open2(url_picin))
    img_url = re.findall(r'><img src="(http://u.thsi.cn/imgsrc/input/.+?png)',allhtml)[0]
    pic_path = '/home/luo/my_bot/799/pic_db/wps.jpg'
    img = url_open2(img_url)
    try:        
        os.system(f'rm {pic_path}')
    except:
        pass
    with open(pic_path,'ab') as f0:
        f0.write(img)
    image = Image.open(pic_path)
    buff = BytesIO()
    image = image.convert('RGB')
    image.save(buff, 'jpeg')
    return b64encode(buff.getvalue()).decode()
    
 
def getthswp():
    url = 'https://ai.iwencai.com/searchapi?q=A%E8%82%A1%E6%94%B6%E8%AF%84&tid=info&p=1&jump=0' #收评
    url_picin = json.loads(url_open3(url))['data']['list'][0]['list'][0]['URL']
    allhtml = str(url_open2(url_picin))
    img_url = re.findall(r'><img src="(http://u.thsi.cn/imgsrc/input/.+?png)',allhtml)[0]
    pic_path = '/home/luo/my_bot/799/pic_db/sps.jpg'
    img = url_open2(img_url)
    try:        
        os.system(f'rm {pic_path}')
    except:
        pass
    with open(pic_path,'ab') as f0:
        f0.write(img)
    image = Image.open(pic_path)
    image = image.convert('RGB')
    buff = BytesIO()
    image.save(buff, 'jpeg')
    return b64encode(buff.getvalue()).decode() 
    
    
    
    
    
    
