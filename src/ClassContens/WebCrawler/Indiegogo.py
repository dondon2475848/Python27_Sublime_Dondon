# coding=utf-8
# 使python可以讀取中文
# 爬取Indiegogo時，被當成機器人，因此要加入User-Agent與Cookie的資訊偽造成網頁的瀏覽者


import requests
import json
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36', 
'Cookie':'romref_referer_host=www.google.com.tw; _gat=1; D_SID=140.115.236.39:BOThEAAGv4SMTbKm8/co88YZjak31qrQ7tzdyKgJePc; __qca=P0-1605812000-1462324323319; _gat_appcues_ga=1; ki_t=1462324326470%3B1462324326470%3B1462324326470%3B1%3B1; ki_r=https%3A%2F%2Fwww.google.com.tw%2F; __hstc=223492548.da3ad0a8cbebf03d8c2cf6eb8e74c4bc.1462324326540.1462324326540.1462324326540.1; __hssrc=1; __hssc=223492548.1.1462324326540; hsfirstvisit=https%3A%2F%2Fwww.indiegogo.com%2F%23%2Fpicks_for_you|https%3A%2F%2Fwww.google.com.tw%2F|1462324326538; hubspotutk=da3ad0a8cbebf03d8c2cf6eb8e74c4bc; utag_main=v_id:015479520f4b001cc99be13543d60506c001a06400bd0$_sn:1$_ss:0$_pn:3%3Bexp-session$_st:1462326200985$ses_id:1462324301643%3Bexp-session; D_PID=D8587F6D-A6E5-34C9-B6C5-17392785DB77; D_IID=AFCA9B4F-118C-3C31-85C2-64870B3773BD; D_UID=4D984B67-BE41-3779-B36B-65F850B3AF4A; D_HID=u+s6X+9Xakv8y5xd1N/CSTkiihPzbzMBdas4g3d2vxs; __ar_v4=; apc_user_call_count=2; romref=ORG_www_TW_XXXX_sch-goog_XXXXXXXX_0002_www.google.com.tw; visitor_id=278cba48720054c263e74725c4dac2f790d7ef50098c8cbbb17866a164ca31a5; analytics_session_id=42b42a11d370e48e31ba2df380104bf5b905a479638b62b652ec904e1b944742; _session_id=c8ab92c626784125d18dd0bcc34120ac; locale=en; cohort=www.google.com.tw%7Csch-goog; recent_project_ids=; _ga=GA1.2.1391222500.1462324318'
}
res = requests.get('https://www.indiegogo.com/private_api/explore?filter_category=Technology&filter_funding=&filter_percent_funded=&filter_quick=popular_all&filter_status=&per_page=12&pg_num=1', headers = headers)
jd = json.loads(res.text)

print jd
# 把title的資料抓出來
for campaign in jd['campaigns']:
    print campaign['title']
