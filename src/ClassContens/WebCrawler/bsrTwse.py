# coding=utf-8
# 使python可以讀取中文
# 台灣證券交易所 分點¶
# http://bsr.twse.com.tw/bshtm/
# 因為前端與後端是分開的，因此不輸入驗證碼，即可以取得資料

import requests

payload = {
'__EVENTTARGET':'',
'__EVENTARGUMENT':'',
'__LASTFOCUS':'',
'__VIEWSTATE':'/wEPDwUJOTAxMjkxMjg3D2QWAgIDD2QWBAIBD2QWAmYPZBYEZg9kFgJmDxAPFgYeB0NoZWNrZWRnHglGb3JlQ29sb3IKAB4EXyFTQgIEZGRkZAIBD2QWAgIBDw8WBB8BCgAfAgIEZGQCAw9kFgQCAw8PFgIeBFRleHQFE+mpl+itieeivOW3sumAvuacny5kZAIJDw8WBh4LTmF2aWdhdGVVcmwFEH4vYnNDb250ZW50LmFzcHgfAwUP5LiL6LyJIDIzMzAgQ1NWHgdWaXNpYmxlaGRkGAIFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBRJSYWRpb0J1dHRvbl9Ob3JtYWwFEFJhZGlvQnV0dG9uX0V4Y2QFEFJhZGlvQnV0dG9uX0V4Y2QFD0NhcHRjaGFDb250cm9sMQ8FJDI4YzA4ZTZjLTBjYTUtNDE5Mi1iODlkLWIyZGFlNWY1MmM5ZWTQPiPnG/NGumK2T5rggKiE',
'__EVENTVALIDATION':'/wEdAAZvT5ifEcFvgmhMO/9jTwGgfMmuxAJNAJcNkRRsVeJwwqKURZav/+YrVMqaWE2hvMxJwK4Ohf3nRgXHkFhQen1PRSciNdPYWmINCrip1wqw01PJCA0uL9aE2sjICZqv6GoQB2GjmROUzjW5eXlpj/QW',
'RadioButton_Normal':'RadioButton_Normal',
'TextBox_Stkno':'2330',
'CaptchaControl1':'JTUPY',
'btnOK':'查詢'
    
}
rs = requests.session()
print rs
# res = rs.post('http://bsr.twse.com.tw/bshtm/bsMenu.aspx', data = payload)
# res2 = rs.get('http://bsr.twse.com.tw/bshtm/bsContent.aspx')
# print res2.text