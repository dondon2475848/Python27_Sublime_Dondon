# coding=utf-8
# 使python可以讀取中文

dic = {'a':1, 'b':2, 'd':100}
print 'a' in dic
print 'c' in dic  


def PrintKeyValue(dic_in):
    for key, value in dic_in.iteritems() :
        print key,'  :  ', value
        
PrintKeyValue(dic)