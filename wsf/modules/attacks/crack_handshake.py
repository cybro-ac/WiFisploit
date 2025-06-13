# wifisploit/modules/crack_handshake.py

import os

a = '\033[0;31m'
b = '\033[0;32m'
c = '\033[0;37m'
d = '\033[1;37m'

handshake = input(f'{d}wsf ({a}HandShake{d})> {c}')
if handshake.lower() == 'back':
	quit()
else:
	print(f'{d}HandShake => {b}{handshake}')

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

wordlist = input(f'{d}wsf ({a}Wordlist{d})> {c}')
if wordlist.lower() == 'back':
	quit()
else:
	print(f'{d}Wordlist => {b}{wordlist}')

os.system(f'aircrack-ng -b {bssid} -c {channel} -w {wordlist} {handshake}')
