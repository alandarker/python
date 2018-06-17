# /!usr/bin/evn python
#  - * -coding:utf-8 -*-
from requests import RequestException

__author__ = '1112'
import requests
import re
import time

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
n=0
page=0
# url = 'http://maoyan.com/board/'
urls='http://maoyan.com/films?'
def get_one_page():
    global page
    # 通过try来捕获并兼容请求错误
    try:
        if not page==0:
            url = 'http://maoyan.com/films?offset={}'.format(page)
            response = requests.get(url, headers=headers)
        else:
            url='http://maoyan.com/films?'
            response = requests.get(url,headers=headers)
        # 通过状态码为 200 判断请求是否成功，成功返回内容，反之返回None
        if response.status_code == 200:
            print('html请求成功',url)
            html = response.text
            return html
        return get_one_page()
    except RequestException:
        # 请求错误都返回 None
        return None
""""
def parse_one_page(html):
    reg=re.compile(r'<dd>.*?board-index-\d+">(\d+)</i>.*?data-src="(.*?)".*?alt="(.*?)".*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?raction">(.*?)</i>.*?</div>',re.S)
    regg=re.findall(reg,html)
    print(type(regg))
    for dan in regg:
        numur=dan[0]+')'
        pictrur=dan[1]
        title=dan[2]
        date=dan[3]
        dital=dan[4]+dan[5]
        name=title+dital+date
        path='E:\\study\Python3.5\\code\\maoyan\\{}.png'.format(name)
        r=requests.get(pictrur)
        # print(numur,pictrur,title,date,dital)
        with open(path, 'wb') as ff:
            ff.write(r.content)
            print('正在下载',title)
    ff.close()
"""
def top_parse():
    global page,n

    m = str(n)
    url=get_one_page()
    reg=re.compile(r'<dd>.*?data-src="(.*?)".*?title="(.*?)">.*?integer">(.*?)</i>.*?fraction">(\d+)</i></div>',re.S)
    beg=re.findall(reg,url)
    for i in beg:
        url=i[0]
        name=i[1]
        point=i[2]+i[3]
        title=m+name+point
        r=requests.get(url)
        print('正在下载',name)
        with open(r'maoyan\{}.jpg'.format(title),'wb') as ff:
            ff.write(r.content)
            n+=1
            m=str(n+1)
    if n%100 == 0:
        time.sleep(15)
    x=30
    page=page+x

    return top_parse()

def main():
    top_parse()

if __name__ == '__main__':
    main()
