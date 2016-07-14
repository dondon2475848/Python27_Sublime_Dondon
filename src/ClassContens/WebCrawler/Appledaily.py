#coding=utf-8

import requests
from bs4 import BeautifulSoup
res = requests.get('http://www.appledaily.com.tw/realtimenews/section/new/')
#print res.text
soup = BeautifulSoup(res.text, "lxml")
for ent in soup.select('li.rtddt'):
    print "============="
#     print ent
#     比較有沒有加[0]的差別，未加[0]是個list，加[0]是將list中第0個unit取出。     list中的中文為unicodes
#     print ent.select('h1')
#     print "..................."
#     print ent.select('h1')[0]
#     print ent.select('h1')[0].text
    print ent.select('h1')[0].text, ent.select('h2')[0].text, ent.select('time')[0].text