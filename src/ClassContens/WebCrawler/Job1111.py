# coding=utf-8
# 使python可以讀取中文

import requests

res = requests.get('http://www.1111.com.tw/job-bank/job-index.asp?ss=s&ks=%E5%A4%A7%E6%95%B8%E6%93%9A&tt=1,2,4,16&si=1&ps=40&trans=1')
# print res.text

from bs4 import BeautifulSoup 
soup = BeautifulSoup(res.text, "lxml") 

# for ul in soup.select('ul'):
#     print ul.find( 'a' )['title'].text  
    
    
# for job in soup.select('li.showPositionCssA'):
#     if len(job.select('a')) > 0:
#         print job.select('a')[0]['title']
#         
    
for job in soup.select('ul'):
        if len(job.select('a.positionCssA')) > 0:
            print job.select('a.positionCssA')[0]['title'],job.select('li.showDatechangeCss')[0].text,job.select('a.listcol2')[0].text,job.select('li.showWorkcityCss')[0].text