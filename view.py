import os

file_path = "/sdcard/hubk/view/view.py"

try:
    os.remove(file_path)
    print("HI BRO...")
except FileNotFoundError:
    print("HELLO...")
except PermissionError:
    print("HMM....")
from urllib.parse import urlencode
import base64
from pystyle import *
import os
import sys
import ssl
import re
import time
import random
import threading
import requests
import hashlib
import json
from urllib3.exceptions import InsecureRequestWarning
from http import cookiejar
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
kt_code = "</>"
dem = 0
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from time import sleep,strftime
from pystyle import *
from time import sleep 
import requests, random
import requests
import base64, json,os
from time import sleep,strftime
import re,requests,os,sys
from time import sleep 
import requests, random
import uuid, re
from pystyle import Write,Colors
import socket
from datetime import datetime
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
xnhac = "\033[1;36m"
#today nand clear
os.system('cls')
data_machine = []
today = date.today()
os.system('clear')
#daystime
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
raofficialvirus = trang + " " + trang + "[" + do + "÷_+" + trang + "] " + trang + "=> "
blue = Col.light_blue
lblue = Colors.StaticMIX((Col.light_green, Col.white, Col.white))
red = Colors.StaticMIX((Col.green, Col.white, Col.white))
def validate_input(input_str):
    # Kiểm tra có chứa ký tự số không
    if any(char.isdigit() for char in input_str):
        return False
        print("\033[31m➤ Tên Tấn Công Không Được Ghi Số !!")
    # Kiểm tra có chứa ký tự đặc biệt không
    return True
    print("\033[31m➤ Tên Tấn Công Không Được Ghi Số !!")
def format_print(symbol, text):
    return f"""                      {Col.Symbol(symbol, lblue, blue)} {lblue}{text}{Col.reset}"""

def format_input(symbol, text):
    return f"""                      {Col.Symbol(symbol, red, blue)} {red}{text}{Col.reset}"""

banner ="""




░██████╗████████╗░█████╗░██████╗░████████╗  ██╗░░██╗███████╗██╗░░░██╗  ██████╗░░░██╗██╗██╗░░██╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝  ██║░██╔╝██╔════╝╚██╗░██╔╝  ╚════██╗░██╔╝██║██║░░██║
╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░  █████═╝░█████╗░░░╚████╔╝░  ░░███╔═╝██╔╝░██║███████║
░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░  ██╔═██╗░██╔══╝░░░░╚██╔╝░░  ██╔══╝░░███████║██╔══██║
██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░  ██║░╚██╗███████╗░░░██║░░░  ███████╗╚════██║██║░░██║
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ╚══════╝░░░░░╚═╝╚═╝░░╚═╝


                                                WELCOME BRO TO MY TOOL 
                                         

\n"""
title = """\n\n\n
         
"""
print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.light_green)), Center.XCenter(title.center(100))) + Colorate.Vertical(Colors.DynamicMIX((Col.light_green, Col.light_blue)), Center.XCenter(banner.center(100))))
print("\033[37m1. \033[32mStart Tool View")
choice = int(input("\033[37m[ \033[31m1 \033[37m]\033[32m Lựa Chọn Của Bạn Là: \033[33m"))

if choice == 1:
    a = now.strftime("%d")
    h = int(now.strftime("%d"))
    ngay_trc = h - 2
    b = now.strftime("%m")
    day = now.strftime("%d-%m-%Y")
    today = now.strftime("%d-%m-%Y")
    d = now.strftime("%d-%m")
    ngay = int(strftime('%d'))
    encodedBytes = base64.b64encode(d.encode("utf-8"))
    key = str(encodedBytes, "utf-8")
    key1 = str(ngay * 12345 + 109)
    key = 'raofficialvirus' + key1
    hentai = (f"https://anhgit.site/key/?key={key}")
    api_token = 'd526e69bae943971eba13d768807e63872fa871c'
    url = requests.get(f'https://link1s.com/api?api={api_token}&url={hentai}').json()
    status = url['status']
    link = url['shortenedUrl']
    file_key = f'key_ngay{ngay_hom_nay}.txt'
    file_key_cu = f'key_ngay{ngay_trc}.txt'
    check_file_key = os.path.exists(file_key)
    
    if check_file_key == False:
        print(f"{raofficialvirus}{luc}Do Đây Là Tool Share Free Nên Key Sẽ Thay Đổi Mỗi Ngày !!")
        print(f'{raofficialvirus}{luc}Truy Cập Vào Link{trang}: {link} {luc}Để Lấy Key Miễn Phí')
        print(f'{trang}-----------------------------------------------------------------')
        print(f'\033[1;36m╔════════════════════════╗')
        print(f'\033[1;36m║\033[1;33mNhập Key Ngày \033[1;37m{today}\033[1;36m║')
        print (f"\033[1;36m║════════════════════════╝")
        
        while True:
            ma = input(f"{xnhac}╚══════➩ \033[1;33m")
            
            if ma == key:
                print(f'{raofficialvirus}{luc}API Key Chính Xác')
                os.system("cls" if os.name == "nt" else "clear")

                luu = open(file_key, 'a+')
                luu.write(ma)
                luu.close()
                break
            elif ma != key:
                print(f'{raofficialvirus}{do}API Key Sai')
                
    elif check_file_key == True:
        print(f'{raofficialvirus}{luc}Đang Lấy Key...', end='\r')
        sleep(1)
        k = open(file_key, 'r')
        ma = k.read()
        k.close()
        
        if ma == key:
            print(f'{raofficialvirus}{luc}Lấy Key Thành Công       ', end='\r')
            sleep(0.5)
        elif ma != key:
            if os.path.exists(file_key_cu) == True:
                os.system(f'rm {file_key_cu}')
            os.system(f'rm {file_key}')
            print(f'{raofficialvirus}{do}API Key Sai         ')
            
            while True:
                ma = input(f"{raofficialvirus}{luc}Nhập API Key\033[1;32m Ngày \033[1;37m{today}: \033[1;33m")
                
                if ma == key:
                    print(f'{raofficialvirus}{luc}API Key Chính Xác')
                    os.system("cls" if os.name == "nt" else "clear")

                    luu = open(file_key, 'a+')
                    luu.write(ma)
                    luu.close()
                    break
                elif ma != key:
                    print(f'{raofficialvirus}{do}API Key Sai           ')
                    exit()
if choice == 8:
    a = now.strftime("%d")
    h = int(now.strftime("%d"))
    ngay_trc = h - 2
    b = now.strftime("%m")
    day = now.strftime("%d-%m-%Y")
    today = now.strftime("%d-%m-%Y")
    d = now.strftime("%d-%m")
    ngay = int(strftime('%d'))
    encodedBytes = base64.b64encode(d.encode("utf-8"))
    key = str(encodedBytes, "utf-8")
    key1 = str(ngay * 12345 + 109)
    key = 'raofficialvirus' + key1
    key = 'admin080'
    hentai = (f"https://anhgit.site/key/?key={key}")
    api_token = 'd526e69bae943971eba13d768807e63872fa871c'
    url = requests.get(f'https://link1s.com/api?api={api_token}&url={hentai}').json()
    status = url['status']
    link = url['shortenedUrl']
    file_key = f'key_ngay1_{ngay_hom_nay}.txt'
    file_key_cu = f'key_ngay1_{ngay_trc}.txt'
    check_file_key = os.path.exists(file_key)
    
    if check_file_key == False:
        print(f"{raofficialvirus}{luc}Do Đây Là Tool Share Free Nên Key Sẽ Thay Đổi Mỗi Ngày !!")
        print(f'{raofficialvirus}{luc}Truy Cập Vào Link{trang}: {link} {luc}Để Lấy Key Miễn Phí')
        print(f'{trang}-----------------------------------------------------------------')
        print(f'\033[1;36m╔════════════════════════╗')
        print(f'\033[1;36m║\033[1;33mNhập Key Ngày \033[1;37m{today}\033[1;36m║')
        print (f"\033[1;36m║════════════════════════╝")
        
        while True:
            ma = input(f"{xnhac}╚══════➩ \033[1;33m")
            
            if ma == key:
                print(f'{raofficialvirus}{luc}API Key Chính Xác')
                os.system("cls" if os.name == "nt" else "clear")

                luu = open(file_key, 'a+')
                luu.write(ma)
                luu.close()
                break
            elif ma != key:
                print(f'{raofficialvirus}{do}API Key Sai')
                
    elif check_file_key == True:
        print(f'{raofficialvirus}{luc}Đang Lấy Key...', end='\r')
        sleep(1)
        k = open(file_key, 'r')
        ma = k.read()
        k.close()
        
        if ma == key:
            print(f'{raofficialvirus}{luc}Lấy Key Thành Công       ', end='\r')
            sleep(0.5)
        elif ma != key:
            if os.path.exists(file_key_cu) == True:
                os.system(f'rm {file_key_cu}')
            os.system(f'rm {file_key}')
            print(f'{raofficialvirus}{do}API Key Sai         ')
            
            while True:
                ma = input(f"{raofficialvirus}{luc}Nhập API Key\033[1;32m Ngày \033[1;37m{today}: \033[1;33m")
                
                if ma == key:
                    print(f'{raofficialvirus}{luc}API Key Chính Xác')
                    os.system("cls" if os.name == "nt" else "clear")

                    luu = open(file_key, 'a+')
                    luu.write(ma)
                    luu.close()
                    break
                elif ma != key:
                    print(f'{raofficialvirus}{do}API Key Sai           ')
                    exit()
import requests
def get_ip_info(ip_addr, api_key):
    url = f"http://api.ipstack.com/{ip_addr}?access_key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data
import datetime

now = datetime.datetime.now()
formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
def format_print(symbol, text):
    return f"""                      {Col.Symbol(symbol, lblue, blue)} {lblue}{text}{Col.reset}"""

def format_input(symbol, text):
    return f"""                      {Col.Symbol(symbol, red, blue)} {red}{text}{Col.reset}"""
def banner1():
    os.system("cls" if os.name == "nt" else "clear")
    title = """\n\n\n
"""
    banner1 ="""
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                 │
│                              ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗                              │
│                              ██║   ██║██║██╔══██╗██║   ██║██╔════╝                              │
│                              ██║   ██║██║██████╔╝██║   ██║███████╗                              │
│                              ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║                              │
│                               ╚████╔╝ ██║██║  ██║╚██████╔╝███████║                              │
│                                ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                              │
│                                                                             Boot Script 2.0     │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
\n"""
    print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.light_green)), Center.XCenter(title.center(100))) + Colorate.Vertical(Colors.DynamicMIX((Col.light_green, Col.light_green)), Center.XCenter(banner1.center(100))))
def main():
    ip_address = requests.get('https://api.ipify.org').text
    YOUR_API_KEY = "f8f7016e2d0d474c6f68ad42ce4db926"
    ip_info = get_ip_info(ip_address, YOUR_API_KEY)
    print(f"\033[34mĐịa Chỉ IP:\033[32m {ip_address}")
    print(f"\033[34mKinh Độ:\033[32m {ip_info['longitude']}")
    print(f"\033[34mVĩ Độ:\033[32m {ip_info['latitude']}")
    print(f"\033[34mKhu Vực:\033[32m {ip_info['region_name']}")
    print(f"\033[34mQuốc Gia:\033[32m {ip_info['country_name']}")
    print(f"\033[34mThành Phố:\033[32m {ip_info['city']}")
    print(f"\033[34mMã Vùng:\033[32m {ip_info['zip']}")
class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

r = requests.Session()
r.cookies.set_policy(BlockCookies())

__domains = ["api22-core-c-useast1a.tiktokv.com", "api19-core-c-useast1a.tiktokv.com",
                          "api16-core-c-useast1a.tiktokv.com", "api21-core-c-useast1a.tiktokv.com"]
__devices = ["SM-G9900", "SM-A136U1", "SM-M225FV", "SM-E426B", "SM-M526BR", "SM-M326B", "SM-A528B",
                          "SM-F711B", "SM-F926B", "SM-A037G", "SM-A225F", "SM-M325FV", "SM-A226B", "SM-M426B",
                          "SM-A525F", "SM-N976N"]
__versions = ["190303", "190205", "190204", "190103", "180904", "180804", "180803", "180802",  "270204"]
class Gorgon:
	def __init__(self,params:str,data:str,cookies:str,unix:int)->None:self.unix=unix;self.params=params;self.data=data;self.cookies=cookies
	def hash(self,data:str)->str:
		try:_hash=str(hashlib.md5(data.encode()).hexdigest())
		except Exception:_hash=str(hashlib.md5(data).hexdigest())
		return _hash
	def get_base_string(self)->str:base_str=self.hash(self.params);base_str=base_str+self.hash(self.data)if self.data else base_str+str('0'*32);base_str=base_str+self.hash(self.cookies)if self.cookies else base_str+str('0'*32);return base_str
	def get_value(self)->json:base_str=self.get_base_string();return self.encrypt(base_str)
	def encrypt(self,data:str)->json:
		unix=self.unix;len=20;key=[223,119,185,64,185,155,132,131,209,185,203,209,247,194,185,133,195,208,251,195];param_list=[]
		for i in range(0,12,4):
			temp=data[8*i:8*(i+1)]
			for j in range(4):H=int(temp[j*2:(j+1)*2],16);param_list.append(H)
		param_list.extend([0,6,11,28]);H=int(hex(unix),16);param_list.append((H&4278190080)>>24);param_list.append((H&16711680)>>16);param_list.append((H&65280)>>8);param_list.append((H&255)>>0);eor_result_list=[]
		for (A,B) in zip(param_list,key):eor_result_list.append(A^B)
		for i in range(len):C=self.reverse(eor_result_list[i]);D=eor_result_list[(i+1)%len];E=C^D;F=self.rbit_algorithm(E);H=(F^4294967295^len)&255;eor_result_list[i]=H
		result=''
		for param in eor_result_list:result+=self.hex_string(param)
		return{'X-Gorgon':'0404b0d30000'+result,'X-Khronos':str(unix)}
	def rbit_algorithm(self,num):
		result='';tmp_string=bin(num)[2:]
		while len(tmp_string)<8:tmp_string='0'+tmp_string
		for i in range(0,8):result=result+tmp_string[7-i]
		return int(result,2)
	def hex_string(self,num):
		tmp_string=hex(num)[2:]
		if len(tmp_string)<2:tmp_string='0'+tmp_string
		return tmp_string
	def reverse(self,num):tmp_string=self.hex_string(num);return int(tmp_string[1:]+tmp_string[:1],16)

def send(__device_id, __install_id, cdid, openudid):
    global reqs, _lock, success, fails, rps, rpm
    for x in range(10):
        try:
            version = random.choice(__versions)
            params = urlencode(
                                {
                                    "os_api": "25",
                                    "device_type": random.choice(__devices),
                                    "ssmix": "a",
                                    "manifest_version_code": version,
                                    "dpi": "240",
                                    "region": "VN",
                                    "carrier_region": "VN",
                                    "app_name": "musically_go",
                                    "version_name": "27.2.4",
                                    "timezone_offset": "-28800",
                                    "ab_version": "27.2.4",
                                    "ac2": "wifi",
                                    "ac": "wifi",
                                    "app_type": "normal",
                                    "channel": "googleplay",
                                    "update_version_code": version,
                                    "device_platform": "android",
                                    "iid": __install_id,
                                    "build_number": "27.2.4",
                                    "locale": "vi",
                                    "op_region": "VN",
                                    "version_code": version,
                                    "timezone_name": "Asia/Ho_Chi_Minh",
                                    "device_id": __device_id,
                                    "sys_region": "VN",
                                    "app_language": "vi",
                                    "resolution": "720*1280",
                                    "device_brand": "samsung",
                                    "language": "vi",
                                    "os_version": "7.1.2",
                                    "aid": "1340"
                                }
        )
            payload = f"item_id={__aweme_id}&play_delta=1"
            sig     = Gorgon(params=params, cookies=None, data=None, unix=int(time.time())).get_value()

            proxy = random.choice(proxies) if config['proxy']['use-proxy'] else ""

            response = r.post(
                url = (
                    "https://"
                    +  random.choice(__domains)  +
                    "/aweme/v1/aweme/stats/?" + params
                ),
                data    = payload,
                headers = {'cookie':'sessionid=90c38a59d8076ea0fbc01c8643efbe47','x-gorgon':sig['X-Gorgon'],'x-khronos':sig['X-Khronos'],'user-agent':'okhttp/3.10.0.1'},
                verify  = False,
                proxies = {"http": proxy_format+proxy, "https": proxy_format+proxy} if config['proxy']['use-proxy'] else {}
            )
            reqs += 1
            try:
                if response.json()['status_code'] == 0:
                    _lock.acquire()
                    print(f'{do}[{vang}VIRUS{do}] {do}[{xanh_la}START VIEW SUCCESS{do}] {do}{xanh_duong}+: {trang}{success}{do} View')
                    success += 1
                    _lock.release()
            except:
                if _lock.locked():_lock.release()
                fails += 1
                continue

        except Exception as e:
            pass

def rpsm_loop():
    global rps, rpm
    while True:
        initial = reqs
        time.sleep(1.5)
        rps = round((reqs - initial) / 1.5, 1)
        rpm = round(rps * 60, 1)


def fetch_proxies():
    url_list =[
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks4.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        "https://www.proxy-list.download/api/v1/get?type=socks4",
        "https://www.proxyscan.io/download?type=socks4",
        "https://api.openproxylist.xyz/socks4.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks5.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
        "https://github.com/jetkai/proxy-list/blob/main/archive/txt/proxies-socks5.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
        "https://www.proxy-list.download/api/v1/get?type=socks5",
        "https://www.proxyscan.io/download?type=socks5",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=10000&country=all&ssl=all&anonymity=all",
        
    ]
    for url in url_list :
        response = requests.get(
            url=url
        )
        if response.ok:
            with open("proxies.txt", "a+") as f:
                f.write(response.text)
                f.close()
        else:
            pass

if __name__ == "__main__":
    with open('devices.txt', 'r') as f:
        devices = f.read().splitlines()
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    if config["proxy"]['proxyscrape']:
        fetch_proxies()
    proxy_format = f'{config["proxy"]["proxy-type"].lower()}://{config["proxy"]["credential"]+"@" if config["proxy"]["auth"] else ""}' if config['proxy']['use-proxy'] else ''
    if config['proxy']['use-proxy']:
        with open('proxies.txt', 'r') as f:
            proxies = f.read().splitlines()
    
    banner1()
    print("\033[32mTool By Admin: \033[32mRa 080 Official".center(3))
    print("\033[37m───────────────────────────────────────────────────────────────────────────────────────\033[0m")
    print("\033[34m                                 ⊂👑⊃THÔNG TIN⊂👑⊃\033[0m")
    print("\033[37m───────────────────────────────────────────────────────────────────────────────────────\033[0m")
    main()
    print("\033[34mHôm Nay Là Ngày:\033[32m", formatted_date)
    print("\033[37m───────────────────────────────────────────────────────────────────────────────────────\033[0m")
    try:
        
        
        link = input(f'{do}[{trang}{kt_code}{do}] {xanh_la}Nhập Link Video Cần Chạy: {trang}')
        print(f'{trang}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        __aweme_id = str(
            re.findall(r"(\d{18,19})", link)[0]
            if len(re.findall(r"(\d{18,19})", link)) == 1
            else re.findall(
                r"(\d{18,19})",
                requests.head(link, allow_redirects=True, timeout=1).url
            )[0]
        )
    except:
        exit(f"{do}[{trang}{kt_code}{do}] {do}Không Tìm Thấy Link Hoặc Có Thể Link Sai..!!")
    
    _lock = threading.Lock()
    reqs = 0
    success = 0
    fails = 0
    rpm = 0
    rps = 0
    
    threading.Thread(target=rpsm_loop).start()
    
    
    while True:
        device = random.choice(devices)

        if eval(base64.b64decode("dGhyZWFkaW5nLmFjdGl2ZV9jb3VudCgpIDwgMTAwICMgZG9uJ3QgY2hhbmdlIGNvdW50IG9yIHUgd2lsbCBraWxsIGRldmljZXMgYW5kIHJ1aW4gZnVuIGZvciBvdGhlcnM=")):
            did, iid, cdid, openudid = device.split(':')
            eval(base64.b64decode('dGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9c2VuZCxhcmdzPVtkaWQsaWlkLGNkaWQsb3BlbnVkaWRdKS5zdGFydCgp'))