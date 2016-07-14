# coding=utf-8
# 使python可以讀取中文

import requests
from bs4 import BeautifulSoup as bs
import pandas
res = requests.get('http://www.playsport.cc/visit_member.php?pagetype=predict&visit=gogreen&gameday=today&allianceid=1&path_trace=cD1CWl9NRjtjPW5vX2NvbnMgTUxCILDqu9q9TCA&rp=BZ_MF')
soup = bs(res.text, "lxml")
tb = soup.select('.universe-tablecon')[0]

for tr in tb.select('tr'):
    td = tr.select('td')
    if len(td) == 6:
        print ''.join(td[0].text.split()).strip() 
        
# 
# def getPage(url):
#     domain = 'http://www.playsport.cc'
#     purl = domain + url
#     res = requests.get(purl)
#     print purl
#     soup = bs(res.text, "lxml")
#     tb = soup.select('.universe-tablecon')[0]
# 
#     for tr in tb.select('tr'):
#         td = tr.select('td')
#         if len(td) == 6:
#             print purl, ''.join(td[0].text.split()).strip()         
# #getPage('gogreen')
# 
# res = requests.get('http://www.playsport.cc/buy_predict.php?alli=1&ck=1')
# soup = bs(res.text, "lxml")
# for link in soup.select('.medalpca'):
#     getPage(link['href'])        