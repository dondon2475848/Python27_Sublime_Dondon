#coding=utf-8



import requests
from bs4 import BeautifulSoup
res = requests.get('http://www.1111.com.tw/job-bank/job-index.asp?ss=s&ks=%E5%A4%A7%E6%95%B8%E6%93%9A&tt=1,2,4,16&si=1&ps=40&trans=1')
soup = BeautifulSoup(res.text)
for job in soup.select('#job_result ul')[1:]:   
    print job.select('.showPositionCssA')[0].text, \
          job.select('.showOrganCssA')[0].text, \
          job.select('.showDatechangeCss')[0].text, \
          job.select('.showWorkcityCss')[0].text