import threading
import requests
import random
import re
import json
import pymysql.cursors
import time
import lxml
import os
from bs4 import BeautifulSoup
upsql1 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='',db='bilibili',charset='utf8') #连接到mysql服务器
cursor1 = upsql1.cursor() #创建游标
'''
upsql2 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='',db='bilibili',charset='utf8') #连接到mysql服务器
cursor2 = upsql2.cursor() #创建游标
upsql3 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='',db='bilibili',charset='utf8') #连接到mysql服务器
cursor3 = upsql3.cursor() #创建游标
upsql4 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='',db='bilibili',charset='utf8') #连接到mysql服务器
cursor4 = upsql4.cursor() #创建游标
'''
global mid
global nid
global head
global aid
mid = 123000000 #匹配结束时的aid 123000000
nid = 1657 #从那个aid开始
aid = 0 
head = {
    'Host': 'space.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://space.bilibili.com/146567/',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}
#User-Agent:"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0"
def get_proxy1():
    while True:
        r = requests.get('http://127.0.0.1:8000/?protocol=0&country=国内')
        ip_ports = json.loads(r.text)
        ipadd = random.choice(ip_ports)
        ipsroc = ipadd[2]
        if int(ipsroc) == 10:
            ipadd1 = ipadd[0:2]
            proxy = str(ipadd1[0])+':'+str(ipadd1[1])
            return proxy
def mysql123(payload):
    global head
    global aid
    daili1 = get_proxy1()
    daili = {
        'http' : 'http://'+daili1
    }
    print (daili)
    jscontent = requests.post('http://space.bilibili.com/ajax/member/GetInfo',headers=head,data=payload,proxies = daili)
    vipstr = requests.get('http://space.bilibili.com/ajax/member/getVipStatus?mid='+str(aid),proxies= daili)
    if jscontent == True:
        jsDict = jscontent.json()
        viptype = vipstr.json()
        statusJson = jsDict['status'] if 'status' in jsDict.keys() else False
        vipjsonJson = viptype['status'] if 'status' in viptype.keys() else False
        if vipjsonJson == True:
            if 'data' in viptype.keys():
                vipdatestr = viptype['data']
                vipdate = vipdatestr['vipType']
                vipstatus = vipdatestr['vipStatus']
        if statusJson == True:
            if 'data' in jsDict.keys():
                jsData = jsDict['data']
                mid = jsData['mid']
                name = jsData['name']
                sex = jsData['sex']
                face = jsData['face']
                coins = jsData['coins']
                regtime = jsData['regtime'] if 'regtime' in jsData.keys() else 0
                spacesta = jsData['spacesta']
                birthday = jsData['birthday'] if 'birthday' in jsData.keys() else 'nobirthday'
                place = jsData['place'] if 'place' in jsData.keys() else 'noplace'
                description = jsData['description']
                article = jsData['article']
                fans = jsData['fans']
                friend = jsData['friend']
                attention = jsData['attention']
                sign = jsData['sign']
                attentions = jsData['attentions']
                level = jsData['level_info']['current_level']
                exp = jsData['level_info']['current_exp']
                regtime_format = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(regtime))
                date = (mid, name, sex, face, coins, regtime_format, spacesta, birthday, place, description,article, fans, friend, attention, sign, str(attentions), level, exp, vipdate, vipstatus)
                return date
def main1():
    global mid
    global nid
    global aid
    while nid <= mid:
        aid = nid
        payload = {'mid':aid}
        nid+=1 
        sqldate = mysql123(payload)
        if sqldate:
            sqlstr = 'INSERT INTO user (mid, name, sex, face, coins, regtime, spacesta, birthday, place, description,article, fans, friend, attention, sign, attentions, level, exp,viptype,vipstatus)VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
            print (sqlstr)
            cursor1.execute(sqlstr % sqldate)
            upsql1.commit()
main1()
'''
def main2():
    global mid
    global nid
    global aid
    while nid <= mid:
        aid = nid
        payload = {'mid':aid}
        nid+=1 
        sqldate = mysql123(payload)
        if sqldate:
            sqlstr = 'INSERT INTO user (mid, name, sex, face, coins, regtime, spacesta, birthday, place, description,article, fans, friend, attention, sign, attentions, level, exp,viptype,vipstatus)VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
            cursor2.execute(sqlstr % sqldate)
            upsql2.commit()
def main3():
    global mid
    global nid
    global aid
    while nid <= mid:
        aid = nid
        payload = {'mid':aid}
        nid+=1 
        sqldate = mysql123(payload)
        if sqldate:
            sqlstr = 'INSERT INTO user (mid, name, sex, face, coins, regtime, spacesta, birthday, place, description,article, fans, friend, attention, sign, attentions, level, exp,viptype,vipstatus)VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
            cursor3.execute(sqlstr % sqldate)
            upsql3.commit()
def main4():
    global mid
    global nid
    global aid
    while nid <= mid:
        aid = nid
        payload = {'mid':aid}
        nid+=1 
        sqldate = mysql123(payload)
        if sqldate:
            sqlstr = 'INSERT INTO user (mid, name, sex, face, coins, regtime, spacesta, birthday, place, description,article, fans, friend, attention, sign, attentions, level, exp,viptype,vipstatus)VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
            cursor4.execute(sqlstr % sqldate)
            upsql4.commit()
'''
#t1 = threading.Thread(target=main1)
'''
t2 = threading.Thread(target=main2)
t3 = threading.Thread(target=main3)
t4 = threading.Thread(target=main4)
'''
'''
t5 = threading.Thread(target=main5)
t6 = threading.Thread(target=main6)
t7 = threading.Thread(target=main7)
t8 = threading.Thread(target=main8)
t9 = threading.Thread(target=main9)
t10 = threading.Thread(target=main10)
t11 = threading.Thread(target=main11)
t12 = threading.Thread(target=main12)
t13 = threading.Thread(target=main13)
t14 = threading.Thread(target=main14)
t15 = threading.Thread(target=main15)
t16 = threading.Thread(target=main16)
'''
#启动线程
#t1.start()
'''
t2.start()
t3.start()
t4.start()

t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
t16.start()
upsql1 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor1 = upsql1.cursor() #创建游标
upsql2 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor2 = upsql2.cursor() #创建游标
upsql3 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor3 = upsql3.cursor() #创建游标
upsql4 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor4 = upsql4.cursor() #创建游标
upsql5 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor5 = upsql5.cursor() #创建游标
upsql6 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor6 = upsql6.cursor() #创建游标
upsql7 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor7 = upsql7.cursor() #创建游标
upsql8 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor8 = upsql8.cursor() #创建游标
upsql9 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor9 = upsql9.cursor() #创建游标
upsql10 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor10 = upsql10.cursor() #创建游标
upsql11 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor11 = upsql11.cursor() #创建游标
upsql12 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor12 = upsql12.cursor() #创建游标
upsql13 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor13 = upsql13.cursor() #创建游标
upsql14 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor14 = upsql14.cursor() #创建游标
upsql15 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor15 = upsql15.cursor() #创建游标
upsql16 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
cursor16 = upsql16.cursor() #创建游标
'''