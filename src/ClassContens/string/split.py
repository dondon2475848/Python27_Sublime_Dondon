# coding=utf-8
# 使python可以讀取中文


a = '\t\t string \n\t string \t\t string'
print a
print a.split()
print ''.join(a.split())
print '!'.join(a.split())



a = '123@456@789@qoo@oop@ooo'
print a.split('@')
print a.split('@', 1)
print a.split('@', 2)