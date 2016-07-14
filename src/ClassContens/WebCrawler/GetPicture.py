# coding=utf-8
# 使python可以讀取中文

import requests
import shutil
def savePic(url):
    res = requests.get(url, stream=True)
    fname = url.split('/')[-1]
    with open('comic/'+fname, 'wb') as f:
        shutil.copyfileobj(res.raw, f)
        
        
def getPageComic(url):
    res = requests.get(url)
    res.encoding = 'big5'
    soup = BeautifulSoup(res.text, "lxml")
    imgsrc =  [ele['src'] for ele in soup.select('img') if 'jpg' in ele['src'] and 'cartoonmad' in ele['src']][0]
    savePic(imgsrc)
    nextpage =  soup.select('a.pages')[-1]['href']
    return nextpage  
 

from bs4 import BeautifulSoup
# do
domain = 'http://www.cartoomad.com/comic/'
firstpage = 'http://www.cartoomad.com/comic/115208242016001.html'
nextpage = getPageComic(firstpage)
# while
while 'html' in nextpage: 
    nextpage = getPageComic(domain + nextpage)     

    
    
    