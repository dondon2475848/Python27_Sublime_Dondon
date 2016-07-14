#coding=utf-8

from datetime import datetime
from datetime import timedelta
print datetime.now()
print type(datetime.now())
print datetime.now().strftime('%Y/%m/%d')
print datetime.now().strftime('%Y/%m/%d %H:%M')

print datetime.strptime('2016/05/12','%Y/%m/%d' )



print datetime.now()
print datetime.now() - timedelta(days = 1)


for i in range(1,10):
    #print datetime.now() - timedelta(days = i),
    print (datetime.now() - timedelta(days = i)).strftime('%Y-%m-%d')
    
    
print datetime.now() - datetime.strptime('2000/07/7','%Y/%m/%d' ) 
print (datetime.now() - datetime.strptime('2000/07/7','%Y/%m/%d' )).days

print  datetime.strptime('2016/08/5','%Y/%m/%d' ) - datetime.now() 
print  (datetime.strptime('2016/08/5','%Y/%m/%d' ) - datetime.now()).days 


response_date = '102/12/10 10:30' 
getyear = response_date.split('/', 1) 
print getyear
print getyear[0]
print type(getyear[0])
print int(getyear[0]) + 1911
print str(int(getyear[0]) + 1911)