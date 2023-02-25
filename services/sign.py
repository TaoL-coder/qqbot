import os,re,time,random,requests,datetime
from retrying import retry
import urllib.request as ur
from paddleocr import PaddleOCR
from json import loads,dump,load
from cv2 import filter2D


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
    ret = ur.Request(url,headers=headers)
    response = ur.urlopen(ret)
    html = response.read() #隐藏
    return html

def check_sign(session):
    url = re.findall('url=(.+?)]',session)[0]
    img = url_open(url)
    os.system('rm /home/luo/my_bot/799/pic_db/check_sign_img/xx.jpg')
    with open('/home/luo/my_bot/799/pic_db/check_sign_img/xx.jpg','ab') as f:
        f.write(img)
    
    
def recog_pic():
    ocr = PaddleOCR(use_angle_cls=True, lang="ch",use_gpu=False) # need to run only once to download and load model into memory ,use_gpu=False
    img_path = '/home/luo/my_bot/799/pic_db/check_sign_img/xx.jpg'
    
    result = ocr.ocr(img_path, cls=True)
    
    dir = '/home/luo/my_bot/799/pic_db/subscriber.json'
    tixing_list = []
    
    #buzhun = []
    with open(dir) as f:
        dict_ = load(f)
        for i,j in dict_.items():
            user_id,name_ = i,j[0]
            for line in result:
                if line[1][0] == name_:
                    #if line[1][1] > 0.9:
                    sendkey = j[1]
                    tixing_list.append([user_id,sendkey])
                    #elif line[1][1] < 0.9:
                    #buzhun.append(i)
                    
    return tixing_list
    
 
def create_subscriber(name,user_id,sendkey):
    dir = '/home/luo/my_bot/799/pic_db/subscriber.json'
    with open(dir) as f:
        dict_ = load(f)
    if str(user_id) in dict_:
        return '已经订阅了!不要再尝试啦~~'
    else:
        with open(dir,'w') as f:
            dict_[str(user_id)] = [name,sendkey]
            dump(dict_,f,ensure_ascii=False,sort_keys=True, indent=4)
            return '订阅成功!\n如需退订，直接回复[取消订阅]即可'
            
        
def del_subscriber(user_id):
    dir = '/home/luo/my_bot/799/pic_db/subscriber.json'
    with open(dir) as f:
        dict_ = load(f)
    del dict_[str(user_id)]
    with open(dir,'w') as f:
        dump(dict_,f,ensure_ascii=False,sort_keys=True, indent=4)
        return '退订成功！'
    
    
    
    
    
    
    
    
    