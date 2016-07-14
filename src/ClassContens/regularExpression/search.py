# coding=utf-8
# 使python可以讀取中文

a = '他欠了我 250,000元, 地震了~~~~~~'
b = 'b欠了我 4,000元, 地震了~~~~~~'
c = 'c欠了我 200元, 地震了~~~~~~'
import re
m = re.search('250,000', a)
print m.group(0)

print m.group(0)

print"========================"
print b
m = re.search('[0123456789]', b) # [] 代表 or ... 0 or 1 or 2 .. or 9
print m.group(0)

m = re.search('[0-9]', b) # 0-9 代表 0 ~ 9
print m.group(0)

m = re.search('\d', b) # \d == [0-9]
print m.group(0)

print"========================"
print b
m = re.search('[abcdefghijklmnopqrstuvwxyz]', b) # [] 代表 or ... a or b or z
print m.group(0)

m = re.search('[a-z]', b) # [aabcdefg...z] == [a-z]
print m.group(0)

m = re.search('[a-zA-Z]', b) # 涵蓋大小寫
print m.group(0)

m = re.search('[a-zA-Z0-9]', b) # 涵蓋大小寫, 數字
print m.group(0)

m = re.search('\w', b) # 涵蓋大小寫, 數字 == [a-zA-Z0-9]
print m.group(0)

print"========================"
c = '!@#!@#$'
m = re.search('.', c) # . 萬用字元
print m.group(0)

print"========================"
a = '他欠了我 250,000元, 地震了~~~~~~'
m = re.search('\d{1,2}',a)  # 代表找到1 ~ 2 個數字
print m.group(0)

m = re.search('\d{3}',a)  # 代表找到剛剛好3個數字
print m.group(0)


m = re.search('\d{1,}',a)  # 代表找到1個以上的數字
print m.group(0)

m = re.search('\d+',a)  # {1,} == +
print m.group(0)

m = re.search('\d{0,}',a)  # 代表找到0個以上的數字
print m.group(0)

m = re.search('\d*',a)  # {0,} == *
print m.group(0)

print"========================"
a = '他欠了我 250,000元, 地震了~~~~~~'
m = re.search('[0-9,]+',a)
print m.group(0)


a = '9527欠了我 250,000元, 地震了~~~~~~'
m = re.search('[0-9,]+',a)
print m.group(0)

a = '9527欠了我 250,000元, 地震了~~~~~~'
m = re.search('[0-9,]+元',a)
print m.group(0)

print"========================"
a = '9527欠了我 250,000元, 地震了~~~~~~'
m = re.search('([0-9,]+)元',a)
print m.group(0), m.group(1)
print"========================"
a = ['小明欠了我 250,000元, 地震了~~~~~~', \
    '9527欠了我 4,000元, 地震了~~~~~~',\
    '馬英九欠了我 2,000,000元, 地震了~~~~~~']
for ele in a:
    m = re.search('(.+)欠了我 ([0-9,]+)元',ele)
    print '=========================='
    print m.group(0)
    print m.group(1) # (.+)
    print m.group(2) #([0-9,]+)

print"========================"
phones = ['我的電話是 0912345678 Call Me', '0922-222-222 我餓了', \
          '等妳呦 0911-222333', '真心不騙 09123482384060192381']
for phone in phones:
    m = re.search('09\d+',phone)
    print m.group(0)
print '======================'  
for phone in phones:
    m = re.search('09\d{2}-{0,1}\d{3}-{0,1}\d{3}',phone)
    print m.group(0)
print '======================'  
for phone in phones:
    m = re.search('09\d{2}-?\d{3}-?\d{3}',phone) # {0,1} => ?
    print m.group(0)
    
print '======================'  
# ^ 強制比對開頭, $ 比對結尾
for phone in phones:
    m = re.search('(09\d{2}-?\d{3}-?\d{3})\d*',phone) 
    if m.group(0) == m.group(1):
        print m.group(0),m.group(1)
        
phones = ['0912345678', '0922-222-222', \
          '0911-222333', '09123482384060192381']
print '======================' 
# ^ 強制比對開頭, $ 比對結尾
for phone in phones:
    m = re.search('^09\d{2}-?\d{3}-?\d{3}$',phone) 
    print m.group(0)
print"========================"
from bs4 import BeautifulSoup as bs
dic = {u'底價金額': ''\
      }
with open('gov/51835965.txt', 'r') as f:
    soup = bs(f.read())
    for tr in soup.select('tr'):
        if len(tr.select('th')) > 0:
            if tr.select('th')[0].text.strip() in dic:
                dic[tr.select('th')[0].text.strip()]= tr.select('td')[0].text.strip()

print"========================"
print dic[u'底價金額']

# import re
m = re.search(u'([0-9,]+)元', dic[u'底價金額'])
print m.group(1)
print m.group(1).split(',')
print ''.join(m.group(1).split(','))
print int(''.join(m.group(1).split(',')))
print"========================"
emails  = ['david@largitdata.com', 'qoo@oop.cc', 'qoooop', 'a@yahoo.com']
for email in emails:
    m = re.search('(.+)@(.+)', email)
    if m:
        print m.group(1), m.group(2)
    print m.group(1), m.group(2)
    
print"========================"

print"========================"




