#coding=utf-8
## 蘋果即時新聞
## http://www.appledaily.com.tw/realtimenews/section/new/
import requests
qoo = requests.get('http://www.appledaily.com.tw/realtimenews/section/new/')
print qoo.text
