__author__ = 'Administrator'
#coding=utf-8
import requests
from bs4 import BeautifulSoup
def geturl(url):   #获取下一条页面的url
    r = requests.get(url)
    r.encoding='gb2312'
    html=r.text
    soup = BeautifulSoup(html,"html.parser")
    next_url=soup.find('li',attrs={'class':'fr'})
    mm=next_url.contents
    s=soup.find('a',attrs={'class':'active'})
    for i in mm:
        if i==s:
            n=mm.index(i)
            url='http://newhouse.fang.com'+mm[n+2]['href']
    return url

def one_page(url):    #获取当页中楼盘名称、楼盘位置与楼盘房价
    r = requests.get(url)
    r.encoding='gb2312'
    html=r.text

    soup = BeautifulSoup(html,"html.parser")
    name=soup.find_all('div',attrs={'class':'nlcd_name'})
    address=soup.find_all('div',attrs={'class':'address'})
    price=soup.find_all('div',attrs={'class':'nhouse_price'})

    li1=[] 
    for m in name:    #楼盘名称
        f=m.a.contents
        h=m.a['href']+f[0].strip()
        li1.append(h)
    li2=[]
    for i in address:     #楼盘位置
        li2.append(i.a['title'])
    li3=[]
    for j in price:    #楼盘价格
        pri=j.span.contents
        li3.append(pri[0])

    for i in range(len(li1)):
        print li1[i]+' '+li2[i]+' '+li3[i]

origin_url='http://newhouse.fang.com/house/s/b1pa-b81-b91/?ctm=1.bj.xf_search.page.1'
one_page(origin_url)
url=geturl(origin_url)
index=24  #所有的页数
for i in range(0,index):
    one_page(url)
    url=geturl(url)
