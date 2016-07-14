# coding=utf-8
# 使python可以讀取中文
# 政府電子採購網
# http://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=basic

# 抓取清單完整版
# 引用Package
import requests
from bs4 import BeautifulSoup
import math


# 設定查詢條件
payload={
'method':'search',
'searchMethod':'true',
'searchTarget':'ATM',
'orgName':'',
'orgId':'',
'hid_1':'1',
'tenderName':'',
'tenderId':'',
'tenderStatus':'4,5,21,29',
'tenderWay':'',
'awardAnnounceStartDate':'105/05/04',
'awardAnnounceEndDate':'105/05/04',
'proctrgCate':'3',
'radProctrgCate':'3',
'tenderRange':'',
'minBudget':'',
'maxBudget':'',
'item':'',
'hid_2':'1',
'gottenVendorName':'',
'gottenVendorId':'',
'hid_3':'1',
'submitVendorName':'',
'submitVendorId':'',
'location':'',
'priorityCate':'',
'isReConstruct':'',
'btnQuery':'查詢'    
}
rs = requests.session()
res = rs.post('http://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance', data=payload)
soup = BeautifulSoup(res.text, "lxml")


# 計算抓取頁數
recnumber = int(soup.select('.T11b')[0].text)
pagenumber = int(math.ceil(float(recnumber) / 100))

# 將標案連結存入檔案之中
urlformat = 'http://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance&searchTarget=ATM&method=search&isSpdt=&pageIndex={}'
# 檔案存取位置的絕對路徑 D:\Dropbox\Big_data_develop_class\ETL\Workspace\ClassPratice\WebCrawler
with open('bid_list.txt','w') as f:
    for i in range(1, pagenumber + 1):
        url = urlformat.format(i)
        res2 = rs.get(url)
        soup2 = BeautifulSoup(res2.text, "lxml")
        print_area = soup2.select('#print_area')[0]
        for tr in print_area.select('tr')[1:-1]:        
            f.write('http://web.pcc.gov.tw/tps' +tr.select('a')[0]['href'][2:] + '\n')







