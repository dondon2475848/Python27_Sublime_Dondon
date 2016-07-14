# coding=utf-8
# 使python可以讀取中文

import requests
import shutil
import time
# 創資料夾的語法，先匯入os
import os
# 先檢查資料夾是否存在，不存在再創資料夾
# if  os.path.exists('comic3')==False:
#     os.makedirs('comic3') 

def savePic(url):
    # home 為準備要創立資料夾要放的位置
    home = 'D://Dropbox/Comics/'
    res = requests.get(url, stream=True)
    # document為準備要放漫畫的資料夾之絕對路徑
    document = home+url.split('/')[-2]
    if  os.path.exists(document)==False:
        os.makedirs(document) 
    fname = url.split('-')[-1]
    with open(document+'/'+fname, 'wb') as f:
        shutil.copyfileobj(res.raw, f)
        print "圖片",fname,"已儲存於資料夾",document
        time.sleep(2) 
      
        
def getPageComic(url):
    res = requests.get(url)
    res.encoding = 'big5'
    soup = BeautifulSoup(res.text, "lxml")
#     print soup
    imgsrc =  soup.select('.coverIssue')
#     print imgsrc
    for  jpg  in  imgsrc:  
        src = jpg.find( 'img' )['src']  
#         link = jokes.get( 'src' )  
    savePic(src) 
    
    nextLink =  soup.select('a.nextLink.nextBtn')
    for  nextLink2  in  nextLink:  
        nextPage = nextLink2.get('href')
    return nextPage
 

from bs4 import BeautifulSoup

firstpage = 'http://hellocomic.com/spidey-2016/c1/p1'

nextPage=getPageComic(firstpage)
firstpage_document = firstpage.split('/')[-2]

while firstpage_document in nextPage: 
    nextPage = getPageComic(nextPage)  
 
 
 
