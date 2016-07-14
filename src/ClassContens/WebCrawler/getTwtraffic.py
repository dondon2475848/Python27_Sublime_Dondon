#coding=utf-8
## 台鐵簡易時刻表
## http://twtraffic.tra.gov.tw/twrail/EasySearch.aspx
import requests
res = requests.get('http://twtraffic.tra.gov.tw/twrail/SearchResult.aspx?searchtype=0&searchdate=2016/04/29&fromstation=1810&tostation=1809&trainclass=%271100%27,%271101%27,%271102%27,%271107%27,%271108%27,%271110%27,%271120%27&fromtime=0600&totime=2359')
print res
#印出伺服器狀況
print res.status_code
print res.headers['content-type']
print res.headers['Date']
# 印出選取網站的html的文字
print res.text