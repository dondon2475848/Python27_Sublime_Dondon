# coding=utf-8
# 使python可以讀取中文

with open('data/51830157.txt', 'r') as f:
#     print f.read()
    pass




from bs4 import BeautifulSoup as bs
with open('data/51830157.txt', 'r') as f:
    soup = bs(f.read(), "lxml")
    #print soup.select('tr')
    for tr in soup.select('tr'):
        #print '=================='
        #print tr.select('th')
        if len(tr.select('th')) > 0:
            #print tr.select('th')[0].text
            #print tr.select('th')[0].text.strip()
            if tr.select('th')[0].text.strip() == u'機關代碼':
                
                print tr.select('td')
                print '-------------------'
                print tr.select('td')[0]
                print '-------------------'
                print tr.select('td')[0].text
                print '-------------------'
                print tr.select('td')[0].text.strip()
                
                
with open('data/51830157.txt', 'r') as f:
    soup = bs(f.read(), "lxml")
    for tr in soup.select('tr'):
        if len(tr.select('th')) > 0:
            if tr.select('th')[0].text.strip() == u'機關代碼':
                print tr.select('td')[0].text.strip()
            if tr.select('th')[0].text.strip() == u'機關名稱':
                print tr.select('td')[0].text.strip()


      

dic = {u'機關代碼': '',  u'機關名稱':'', u'單位名稱':'', u'機關地址':''}
with open('data/51830157.txt', 'r') as f:
    soup = bs(f.read(), "lxml")
    for tr in soup.select('tr'):
        if len(tr.select('th')) > 0:
            if tr.select('th')[0].text.strip() in dic:
                #print tr.select('td')[0].text.strip()
                print tr.select('th')[0].text.strip(), tr.select('td')[0].text.strip()    
                
print '=================='                
dic = {u'機關代碼': '',  u'機關名稱':'', u'單位名稱':'', u'機關地址':''}
with open('data/51830157.txt', 'r') as f:
    soup = bs(f.read(), "lxml")
    for tr in soup.select('tr'):
        if len(tr.select('th')) > 0:
            if tr.select('th')[0].text.strip() in dic:
                #print tr.select('td')[0].text.strip()
                dic[tr.select('th')[0].text.strip()]= tr.select('td')[0].text.strip()   
# print dic                
print '=================='
for ele in dic:
    print ele, dic[ele]
    
print '=================='    
dic = {u'機關代碼': '',  u'機關名稱':'', u'單位名稱':'', u'機關地址':'',\
       u'標案案號': '',  u'招標方式':'', u'標的分類':'',\
      }
with open('data/51830157.txt', 'r') as f:
    soup = bs(f.read(), "lxml")
    for tr in soup.select('tr'):
        if len(tr.select('th')) > 0:
            if tr.select('th')[0].text.strip() in dic:
                dic[tr.select('th')[0].text.strip()]= tr.select('td')[0].text.strip()
 

for ele in dic:
    print ele, dic[ele]                
print '==================' 
for ele in dic:
    print ele, repr(dic[ele])
print '==================' 
for ele in dic:
    print ele, ' '.join(dic[ele].split())
print '==================' 

dic = {u'開標時間': ''\
      }

with open('data/51830157.txt', 'r') as f:
    soup = bs(f.read(), "lxml")
    for tr in soup.select('tr'):
        if len(tr.select('th')) > 0:
            if tr.select('th')[0].text.strip() in dic:
                dic[tr.select('th')[0].text.strip()]= tr.select('td')[0].text.strip()


print '==================' 
for ele in dic:
    print ele, dic[ele], type(dic[ele])


print '==================' 
from datetime import datetime
from datetime import timedelta


response_date = '102/12/10 10:30' 
getyear = response_date.split('/', 1) 
print getyear
print getyear[0]
print type(getyear[0])
print int(getyear[0]) + 1911
print str(int(getyear[0]) + 1911)


print str(int(getyear[0]) + 1911) + '/' +getyear[1]

def date_conversion(element):
    getyear = element.split('/', 1) 
    return  datetime.strptime(str(int(getyear[0]) + 1911) + '/' +getyear[1], '%Y/%m/%d %H:%M')

print date_conversion('102/12/10 10:30')


dic = {u'開標時間': ''\
      }
with open('data/51830157.txt', 'r') as f:
    soup = bs(f.read(), "lxml")
    for tr in soup.select('tr'):
        if len(tr.select('th')) > 0:
            if tr.select('th')[0].text.strip() in dic:
                dic[tr.select('th')[0].text.strip()]= tr.select('td')[0].text.strip()

for ele in dic:
    print ele, dic[ele], type(dic[ele])
print dic[u'開標時間']
print date_conversion(dic[u'開標時間'])






                