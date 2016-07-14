# coding=utf-8
# 使python可以讀取中文

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
import json
parsed_json = json.loads(json_string)
print type(parsed_json)