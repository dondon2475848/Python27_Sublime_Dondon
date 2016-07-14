# coding=utf-8
# 使python可以讀取中文

a = u'機關'
b = '機關'
print type(a)
print type(b)
print a ==b
print a.encode('utf-8') == b
print type(a.encode('utf-8'))
print a == u'機關'
print a == b.decode('utf-8')