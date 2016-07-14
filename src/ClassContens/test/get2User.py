# coding=utf-8
# 使python可以讀取中文

import requests
import json
import time




# head = {
#     'User-Agent': 'ai shi ji/5.2.0 (iPhone; iOS 9.3.1; Scale/2.00)User-Agent: ai shi ji/5.2.0 (iPhone; iOS 9.3.1; Scale/2.00)'
# }
# #因為前面的資料都超肥，所以limit先設1玩玩而已
# url = 'https://ifoodie.tw/api/user/?limit=1&offset=0'
# res = requests.get(url, verify=False, headers=head)
# jd = json.loads(res.text, encoding='unicode')
# r = jd['response']
# print r;
# type(r)

url='https://ifoodie.tw/api/user/?limit=2&offset=0'
res = requests.get(url)
resText = res.text.encode('utf-8').replace('{"info": {}, "response": [', '').replace('], "success": true}','')
print resText

# import ast
# ast.literal_eval(resText)

import yaml
d = yaml.load(resText)