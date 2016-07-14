# coding=utf-8
# 使python可以讀取中文

a= '         aaa          '
print a.strip()
print a.lstrip()
print a.rstrip()

b = '!12345!'
print b.strip('!')

c = 'hihiabcabc'
print c.strip('hi')