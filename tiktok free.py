import requests,sys,os,random
bad,good,band,retry,hit=0,0,0,0,0
iid=input('Id : ')
tok=input('Token : ')
os.system("clear")
def tlg(username,res):
    global hit
    hit+=1
    ff = f'''
¸¸.•´¯•.¸ 🇮🇶¸.•´¯•.¸¸ 
𝙷𝙸𝚃 ☊ : {hit} 
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 :{username}
¸¸.•´¯•.¸ 🇮🇶¸.•´¯•.¸¸
Py- @AHMED_KHANA
    '''
#    print(ff)

    requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(ff))
def fil(username):
  global bad,good,band,retry
  url=f'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/unique/id/check/?unique_id={username}&request_tag_from=h5&manifest_version_code=350302&_rticket=1757684077605&app_language=ar&app_type=normal&iid=7477881563939030802&channel=googleplay&device_type=HRY-LX1MEB&language=ar&host_abi=arm64-v8a&locale=ar&resolution=1080*2139&openudid=94d30fe1fa54ad3c&update_version_code=350302&ac2=wifi&cdid=9066ae9d-784c-47c3-ab9e-cc33e6899d69&sys_region=IQ&os_api=29&timezone_name=Asia%2FBaghdad&dpi=480&ac=wifi&device_id=7398181346055390726&os_version=12&timezone_offset=10800&version_code=350302&app_name=musically_go&ab_version=35.3.2&version_name=35.3.2&device_brand=HONOR&op_region=IQ&ssmix=a&device_platform=android&build_number=35.3.2&region=IQ&aid=1340&ts=1757683809'
  headers = {
            'x-tt-req-timeout': '90000',
            'accept-encoding': 'gzip',
            'sdk-version': '2',
            'X-Tt-Token':'03b8a911992c1f856fb544e8ef396ce670054d3189ef4067d5b0c759356503ad2536e72e2a7af32bd7c45806cc63fe93f5ffde6cca9aa590f8a5f0c6acac7f6d9ac77deab2de502cd9503e92871d4ae67b20061663f44e0804845b167657daa1f8d8f--0a4e0a202483bc1c82bfa4acf98ca8d5f5a6c2f0e707cba277855a435e21443ad80b872e12205385f98ce038011ba9fbd89d9cd4277af9d93a32db02e33aba53c4bf322b316e1801220674696b746f6b-3.0.0',
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
    	try:
    		username=uk+mk
    		chk(username)
    	except:pass
from threading import Thread as hh
for i in range(8):
	hh(target=hso).start()    
