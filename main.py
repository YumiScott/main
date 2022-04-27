import os
import time
import requests
from time import sleep

#IP,CN,LOC
_____vinny = print
_____vin = requests.get('http://ipinfo.io/json').json()


def _____kontol_____():
	_____vinny("                       _____          _____ \n__________________________(_)________ __  /_\n__  ___/_  ___/__  ___/__  / ___  __ \_  __/\n_(__  ) / /__  _  /    _  /  __  /_/ // /_  \n/____/  \___/  /_/     /_/   _  .___/ \__/  \n                             /_/")
	
def _____menu_____():
	os.system("clear")
	_____kontol_____()
	_____vinny("")
	_____vinny("[1] Geser bulan pake pake termux")
	_____vinny("[2] Masuk facebook random")
	_____yumi_____ = input ("Pilih : ")
	if _____yumi_____ in [""," "]:
			_____vinny("Jangan kosong")
	elif _____yumi_____ in ['1','01']:
		_____bulan_____()
	elif _____yumi_____ in ['2','02']:
		_____facebook_____()

def _____bulan_____():
	sleep(0.9)
	_____vinny("|__proses mengeser 🌒")
	sleep(0.9)
	_____vinny("|__proses mengeser 🌒")
	sleep(0.9)
	_____vinny("|__proses mengeser 🌒")
	sleep(0.9)
	_____vinny("|__proses mengeser 🌒")
	_____vinny("\__berhasil menggeser bulan 🌒 >_<")
	_____vinny("Tunggu sedang membuka web bokep")
	os.system("xdg-open xnxx.com")
	
def _____facebook_____():
	sleep(0.9)
	_____vinny("|__proses membuka akun facebooo orang")
	sleep(0.9)
	_____vinny("|__proses membuka akun facebooo orang")
	sleep(0.9)
	_____vinny("|__proses membuka akun facebooo orang")
	sleep(0.9)
	_____vinny("|__proses selesai tunggu beberapa detik anda akan diarahkan ke facebook")
	os.system("xdg-open https://m.facebook.com/login")
		
if __name__=="__main__":
	_____menu_____()
