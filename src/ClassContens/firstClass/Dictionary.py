#coding=utf-8
dic = {'a':100, 'b':"yes", 'c':0.98, 'a':600} 
print dic['c']
print dic.keys()
print dic.values()
print dic.get('c')
dic2 = dic
print dic2


dic['d'] = 811
print dic
dic.update({'e':'string'})
print dic

for key in dic:
    print key,dic[key]
print dic2

def func(x):
    return {'a': 1,'b': 2}.get(x) 

func('b')


