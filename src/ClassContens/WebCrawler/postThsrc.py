#coding=utf-8
## 高鐵資料查詢
import requests
payload ={
'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
'EndStation':'fbd828d8-b1da-4b06-a3bd-680cdca4d2cd',
'SearchDate':'2016/04/29',
'SearchTime':'11:00',
'SearchWay':'DepartureInMandarin'
}
res = requests.post('https://www.thsrc.com.tw/tw/TimeTable/SearchResult', data=payload)
# 印出選取網站的html的文字
print res.text