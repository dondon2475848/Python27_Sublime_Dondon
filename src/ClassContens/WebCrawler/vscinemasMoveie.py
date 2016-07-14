# coding=utf-8
# 使python可以讀取中文

import requests
res = requests.get('http://www.ambassador.com.tw/showtime_list.html')
# print res.text 

from bs4 import BeautifulSoup 
soup = BeautifulSoup(res.text, "lxml") 
 
for div in soup.select('div.col-md-10.a'):
#     寫法一：
#     抓'.title'
#     print div.select('.title')[0].text,div.select('.date')[0].text,div.select('.author')[0].text
#     寫法二
    print div.text
#     print div.select('a')[0].text,div.select('.date')[0].text,div.select('.author')[0].text