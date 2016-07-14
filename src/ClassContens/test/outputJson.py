import requests
import json
import time
import copy

start = time.time()
head = {
    'User-Agent': 'ai shi ji/5.2.0 (iPhone; iOS 9.3.1; Scale/2.00)User-Agent: ai shi ji/5.2.0 (iPhone; iOS 9.3.1; Scale/2.00)'
}
#因為前面的資料都超肥，所以limit先設1玩玩而已
url = 'https://ifoodie.tw/api/user/?limit=1&offset=0'
res = requests.get(url, verify=False, headers=head)
jd = json.loads(res.text, encoding='unicode')
r = jd['response']
#粉絲名錄
follow = 'https://ifoodie.tw/api/follow/?limit={}&offset={}&rtn_type=user&target_user_id={}'
#收藏的根目錄，要從這裡才能找到收藏清單、推薦餐廳、曾經到訪這三個資料夾的id
collect = 'https://ifoodie.tw/api/collection/?all=true&user_id={}'
#收藏清單、推薦餐廳、曾經到訪的連結格式都一樣，只差在各有個不同的id
restaurant = 'https://ifoodie.tw/api/collection/{}/blogs/?limit={}&offset={}'
#寫過的所有文章清單
blog = 'https://ifoodie.tw/api/user/{}/blogs/?limit={}&offset={}'

#沒事寫好玩的函數，丟掉不要的key
def extract(d):
    d['_id'] = d['id']
    d.pop('id', None)
    d.pop('profile_pic', None)
    d.pop('thumb', None)
    d.pop('cover_url', None)
    d.pop('profile_pic_origin', None)

#開始爬，暫時先沒翻，要翻的話用個迴圈包起來就好
for i in r:
    extract(i)
    track = []
    x = 0
    #翻粉絲清單，每次翻300個，直到翻完為止
    while True:
        followList = follow.format(x+300, x, i['_id'])
        followRes = requests.get(followList, verify=False, headers=head)
        jdFollow = json.loads(followRes.text, encoding='unicode')
        rf = jdFollow['response']
        for rfi in rf:
            track.append(rfi['id'])
        if len(rf) < 300:
            break
        x += 300
    i['follow'] = track
    article = []
    x = 0
    #翻文章清單
    while True:
        blogList = blog.format(i['_id'], x+300, x)
        blogRes = requests.get(blogList, verify=False, headers=head)
        jdBlog = json.loads(blogRes.text, encoding='unicode')
        rb = jdBlog['response']
        for rbi in rb:
            article.append(rbi['url'])
        if len(rb) < 300:
            break
        x += 300
    i['blog'] = article
    #幫收藏根目錄補上使用者id
    collectionList = collect.format(i['_id'])
    collectRes = requests.get(collectionList, verify=False, headers=head)
    jdCollection = json.loads(collectRes.text, encoding='unicode')
    rc = jdCollection['response']
    #只抓前三個，依序為收藏、推薦、到訪
    for j in xrange(0,3):
        restList = []
        x = 0
        #翻頁+爬資料
        while True:
            restReq = restaurant.format(rc[j]['id'], x+300, x)
            restRes = requests.get(restReq, verify=False, headers=head)
            jdRestaurant = json.loads(restRes.text, encoding='unicode')
            rr = jdRestaurant['response']
            #存餐騰基本資料
            for rri in rr:
                restDict = {}
                try:
                    restDict['city'] = rri['restaurant']['city']
                    restDict['name'] = rri['restaurant']['name']
                    restDict['address'] = rri['restaurant']['address']
                    restDict['lat'] = rri['restaurant']['lat']
                    restDict['lng'] = rri['restaurant']['lng']
                    restDict['id'] = rri['restaurant']['id']
                    restList.append(restDict)
                #有的食記所寫的餐廳沒有任何資訊（數量不多），於是無視他
                except:
                    print "Null"
            if len(rr) < 300:
                break
            x += 300
        #收藏
        if j == 0:
            i['collection'] = copy.deepcopy(restList)
        #推薦
        elif j == 1:
            i['recommendation'] = copy.deepcopy(restList)
        #到訪
        elif j == 2:
            i['visit'] = copy.deepcopy(restList)
    #輸出成json檔
    try:
        with open('ifood.json','w') as f:
            json.dump(i, f)
    #原本寫來接mongoDB用的，怕忘記所以留著
    except:
        print 'Duplicate Element'
end = time.time()
print end - start
