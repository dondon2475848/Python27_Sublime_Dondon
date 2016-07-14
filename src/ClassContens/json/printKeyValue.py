# coding=utf-8
# 使python可以讀取中文
import json

data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
}

json_str = json.dumps(data)
data = json.loads(json_str)


for key, value in data.iteritems() :
    print key, value