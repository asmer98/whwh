#==========[الاصدار السادس]============
import requests,random,telebot,os
#-----------------------------------------------#
good,bad,band,retry=0,0,0,0
id='1427563876'
token ='8092054503:AAGa0OrkwhjUm1YTfuLn9kX5Nzvzfj_Lm04'
#-----------------------------------------------#

def filter(username):
  #tok='0301c1ce3296ed09b2ccb4c3b00d4904b5050a9cda5a23680b8b65f04f363a5e6efb09140b58530fb64f36849ada13ed123e3f14e1254fec190ee3492d01580fdb98de47493b6f45efeb2bb346a8af1f8e2f175ba3eae70ff1078f5b35ae61609765d-CkBhOTBjY2MxMjNjOTY3YjNhYjk3ZTVjODk4MmEwNWUyOWQyMjZjMDAyNmE1ODNlOTQwZjQxZDY2MWMzMzgwMjQ4-2.0.0'
  url=f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/unique/id/check/?unique_id={username}&request_tag_from=h5&manifest_version_code=350302&_rticket=1739455289526&app_language=ar&app_type=normal&iid=7398181872725722886&channel=googleplay&device_type=HRY-LX1MEB&language=ar&host_abi=arm64-v8a&locale=ar&resolution=1080*2139&openudid=94d30fe1fa54ad3c&update_version_code=350302&ac2=wifi&cdid=70390870-9e9d-4479-8661-a5f371645149&sys_region=IQ&os_api=29&timezone_name=Asia%2FBaghdad&dpi=480&ac=wifi&device_id=7398181346055390726&os_version=12&timezone_offset=10800&version_code=350302&app_name=musically_go&ab_version=35.3.2&version_name=35.3.2&device_brand=HONOR&op_region=IQ&ssmix=a&device_platform=android&build_number=35.3.2&region=IQ&aid=1340&ts=1739455236'
  headers = {
                    'x-tt-req-timeout': '90000',
                    'accept-encoding': 'gzip',
                    'sdk-version': '2',
                    'x-tt-token': '0301c1ce3296ed09b2ccb4c3b00d4904b5050a9cda5a23680b8b65f04f363a5e6efb09140b58530fb64f36849ada13ed123e3f14e1254fec190ee3492d01580fdb98de47493b6f45efeb2bb346a8af1f8e2f175ba3eae70ff1078f5b35ae61609765d-CkBhOTBjY2MxMjNjOTY3YjNhYjk3ZTVjODk4MmEwNWUyOWQyMjZjMDAyNmE1ODNlOTQwZjQxZDY2MWMzMzgwMjQ4-2.0.0',
                    'user-agent': 'user-agent: com.zhiliaoapp.musically.go/330802 (Linux; U; Android 12; en_US; M2010J19CG; Build/SKQ1.211202.001;tt-ok/3.12.13.2-alpha.68-quictest) ',
                }
                
  try:response = requests.get(url,cookies=None,headers=headers,).text
  except:print('لايتوفر اتصال في الانترنت')
  #الاتصال
  if '"is_valid":true' in response:return True
  elif '"is_valid":false' in response:return False
  elif response == '':return 'retry'
#-----------------------------------------------#
def chk(username):
  try:response = requests.get(f'https://tiktok.com/@{username}',headers = {'User-Agent': "Mozilla/5.0 (Windos; CPU Mac OS 17_9_82 like Linux OS X) AppleWebKit/397.7.93 (KHTML, like Gecko) Version/29.8 Mobile/15E148 FireFox/899.9"}).text
  except:print('لايتوفر اتصال في الانترنت')
  if '"nickname":' in response:return False
  else:return True
#-----------------------------------------------#
def check(username):
  try:
	  req = chk(username)
	  if req == True:
	    response = filter(username)
	    if response == True:
	      return True
	    elif response == False:
	      return 'band'
	    elif response == 'retry':
	      return 'retry'
	  else:return False
  except:print('no intrnit')
    
#-----------------------------------------------#
def all():
  logo= '''\033[96m░█████╗░██╗░░██╗███╗░░░███╗███████╗██████╗░
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
  global good,bad,band,retry
  while True:
    uk=''.join(random.choice('qwertyuiop1234567890asdfghjkl')for i in range(4))
    mk=''.join(random.choice('qwertyuiopasdfghjklzxcvbnm123456789')for i in range(1))
    lo=''.join(random.choice('123456wertyuiopasdfghjklzxcvbnm789')for i in range(1))
    username=uk
    req=check(username)
    if req == True:
      
      good+=1
      tlg=f'- AHMED Get New Hit : {username}\n- By : @AHMED_KHANA'
      telebot.TeleBot(token).send_message(id,str(tlg))
      with open('h.txt','+a')as j:
        j.write(str(tlg)+'\n')
      with open('hitTIK.txt','a') as f:
        f.write(username+'\n')
    elif req == 'band':
      band+=1
    elif req == False:
      bad+=1
    elif req == 'retry':
      retry+=1
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f'{logo}\n\033[96m====================\n\033[92mGood : \033[1;97m{good}\n\033[91mBad : \033[1;97m{bad}\n\033[94mBand : \033[1;97m{band}\n\033[95mRetry : \033[1;97m{retry}\n\033[96m====================\n\033[1mProgrammer : \033[93mAHMED_KHANA\n{username}')
    #print(f'Good : \033[1;97m{good}\033[91m ~ Bad : \033[1;97m{bad}\033[94m ~ Band : \033[1;97m{band}\033[95m ~ Retry : \033[1;97m{retry}\033[96m ')
#-----------------------------------------------#
from threading import Thread as hso
for i in range(10):
  hso(target=all).start()
