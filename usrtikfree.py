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
import requests,sys,os,random
bad,good,band,retry,hit=0,0,0,0,0
iid=input(X+'Id : ')
tok=input(M+'Token : ')
os.system('clear')
def tlg(username,res):
    global hit
    hit+=1
    ff = f'''
¸¸.•´¯•.¸ AHMED¸.•´¯•.¸¸ 
𝙷𝙸𝚃 ☊ : {hit} 
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 :{username}
¸¸.•´¯•.¸ KHAN¸.•´¯•.¸¸
Py- @AHMED_KHANA
    '''
#    print(ff)

    requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(ff))
def fil(username):
  global bad,good,band,retry
  url=f'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/unique/id/check/?unique_id={username}&request_tag_from=h5&manifest_version_code=350302&_rticket=1739456305098&app_language=ar&app_type=normal&iid=7398181872725722886&channel=googleplay&device_type=HRY-LX1MEB&language=ar&host_abi=arm64-v8a&locale=ar&resolution=1080*2139&openudid=94d30fe1fa54ad3c&update_version_code=350302&ac2=wifi&cdid=70390870-9e9d-4479-8661-a5f371645149&sys_region=IQ&os_api=29&timezone_name=Asia%2FBaghdad&dpi=480&ac=wifi&device_id=7398181346055390726&os_version=12&timezone_offset=10800&version_code=350302&app_name=musically_go&ab_version=35.3.2&version_name=35.3.2&device_brand=HONOR&op_region=IQ&ssmix=a&device_platform=android&build_number=35.3.2&region=IQ&aid=1340&ts=1739456168'
  headers = {
            'x-tt-req-timeout': '90000',
            'accept-encoding': 'gzip',
            'sdk-version': '2',
            'X-Tt-Token':'03b4473d5ce9c9e134050c4d1e3b6dab480474abf576bfb6044760760ae96dbaa22bfa1c927df00224cfd0ac5d712a0f704bb48f148c97eb9846a8154ea659702fbb48e9441d0c6a691790fb4312add9e7764c70fe93b3de2bf3b9b9d24dd1db84645-CkBlYTYzZmFlMzcyOTg1ZTYwNGY5MThjNTM2MmU4NGI1ZDRiYmM0MGFmNThjOGZlOGZlMTk1M2MzNGQyN2U4MmY2-2.0.0',
            'user-agent': 'user-agent: com.zhiliaoapp.musically.go/330802 (Linux; U; Android 12; en_US; M2010J19CG; Build/SKQ1.211202.001;tt-ok/3.12.13.2-alpha.68-quictest) ',
        }
  try:res = requests.get(url,cookies=None,headers=headers,).text
  except:sys.stdout.write('\rno intrnit'),sys.stdout.flush()
  os.system('clear')
  sys.stdout.write(f'\r{res}'),sys.stdout.flush()
  #الاتصال
  if '"is_valid":true' in res:
  	tlg(username,res)
  	good+=1
  	sys.stdout.write(f'\rTrue : {good} False :  {bad} Else : {bad} Block : {retry} '),sys.stdout.flush()
  elif '"is_valid":false' in res:
  	bad+=1
  	sys.stdout.write(f'\rTrue : {good} False :  {band} Else : {bad} Block : {retry} '),sys.stdout.flush()
  	
  
  elif res == ''or '{}':
  	retry+=1
  	sys.stdout.write(f'\rTrue : {good} False :  {band} Else : {bad} Block : {retry} '),sys.stdout.flush()
def chk(username):
  global bad,good,band,retry
  try:response = requests.get(f'https://tiktok.com/@{username}',headers = {'User-Agent': "Mozilla/5.0 (Windos; CPU Mac OS 17_9_82 like Linux OS X) AppleWebKit/397.7.93 (KHTML, like Gecko) Version/29.8 Mobile/15E148 FireFox/899.9"}).text
  except:print('No net')
  if '"nickname":' in response:
  	band+=1
  	sys.stdout.write(f'\rTrue : {good} False :  {band} Else : {bad} Block : {retry} '),sys.stdout.flush()
  else:
  	fil(username)
  	
def hso():
    while True:
    	uk=''.join(random.choice('qwertyuiopasdfghjklzxcvbnm')for i in range(1))
    	mk=''.join(random.choice('qwertyuiopasdfghjklzxcvbnm123456789')for i in range(4))
    	lo=''.join(random.choice('123456789')for i in range(1))
    	username=uk+mk
    	chk(username)
from threading import Thread as hh
for i in range(10):
	hh(target=hso).start()    
