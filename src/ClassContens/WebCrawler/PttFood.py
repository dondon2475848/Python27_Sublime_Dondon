#coding=utf-8

import requests
res = requests.get('https://www.ptt.cc/bbs/Food/index.html')
# print res.text

from bs4 import BeautifulSoup 
soup = BeautifulSoup(res.text, "lxml") 
# print soup
print "共有",len(soup.select('div.r-ent')),"筆，分別為："
dic={}
for div in soup.select('div.r-ent'):
#     寫法一：
#     抓'.title'
#     print div.select('.title')[0].text,div.select('.date')[0].text,div.select('.author')[0].text
#     寫法二

    print div.select('a')[0].text.encode('utf-8'),div.select('.date')[0].text.encode('utf-8'),div.select('.author')[0].text.encode('utf-8')
