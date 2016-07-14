# #coding=utf-8
# 
fid = open('D:\Dropbox\Big_data_develop_class\ETL\Workspace\file\test.txt', 'w')
fid.write('Hello\nWorld')
fid.close()
# 
# 
# fid = open('test.txt', 'r')
# for line in fid: # Using file identifier as iterator
#     print("Line: " + line.strip())
#   
# for line in fid:
# print line
# fid.close()
# 
# a = '\n\taaattt\n\t'
# print a
# print a.strip()
# 
# fid = open('test.txt', 'r')
# lines = fid.readlines()
# for line in lines:
#     print("Line: " + line.strip())
# fid.close()
# 
# 
# for line in lines:
#     print line
# 
# 
# try:
#     fid = open('test.txt', 'r')
#     k
# finally:
#     print 'fid closed'
#     fid.close()
# 
# 
# with open('test.txt', 'r') as f:
#     for line in f:
#         print line.strip()
# 
# 
# with open('test.txt', 'r') as f:
#     k = 0
#     for line in f:
#         k += 1
#     print(k)
# 
# with open('test.txt','r') as f:
#     print len(f.readlines())

# with open('test2.txt','a') as f:
#     f.write('aaaaaaaaaaa')




text = '''Amazon has long favored growth over profits, and in its nearly 22-year lifespan, the company has poured resources into building out a sprawling logistics infrastructure dedicated to giving you what you want almost immediately. Why should you have to wait for days (or, God forbid, leave your house) when you need toilet paper?

Stephenie Landry is the force responsible for the instantaneousness of your gratification—as vice president of Amazon Prime Now, she conceptualized how the company would bring one-hour deliveries to life and assembled the team to work on the problem. “We have something at Amazon called the working-backward process,” Landry says. “We write a press release saying what we would announce to the world, and when I was writing the product concept, I wrote that the experience of Prime Now would be ‘magical.’” Since launching in December 2014, the service has gone live in four countries and more than 30 metropolitan areas around the world. And, as rumors swirl that Amazon may also be working on a global delivery network, Prime Now increasingly looks to be a scaled-down version of the company’s long-term play: to be in complete control of the flow of products in its supply chain, from factories in China and India all the way to your doorstep. That grand plan would involve not only trucks, cargo planes, and drones but also hundreds of thousands of humans working in warehouses and as couriers. And if anything like that aspirational picture of Prime Now actually emerges, UPS and FedEx should probably start prepping their contingency plans as soon as, well, now. —Davey Alba
'''
words = text.split(' ')

dic = {}
for w in words:
    if w not in dic:
        dic[w] = 1
    else:
        dic[w] += 1
print dic


    

from collections import Counter
c = Counter(words)
print c

import operator
sorted_x = sorted(c.items(), key=operator.itemgetter(1), reverse=True)
print sorted_x[0:5]


c.items()














