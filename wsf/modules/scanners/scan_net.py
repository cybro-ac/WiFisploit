# wifisploit/modules/scan_all.py

import os

a = '\033[0;31m'
b = '\033[0;32m'
c = '\033[0;37m'
d = '\033[1;37m'

interface = input(f'{d}wsf ({a}Interface{d})> {c}')
if interface.lower() == 'back':
	quit()
else:
	print(f'{d}Interface => {b}{interface}')
bssid = input(f'{d}wsf ({a}BSSID{d})> {c}')
if bssid.lower() == 'back':
	quit()
else:
	print(f'{d}BSSID => {b}{bssid}')

os.system(f'airodump-ng --bssid {bssid} -M {interface}')
