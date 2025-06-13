# wifisploit/modules/net_discover.py

import os

a = '\033[0;31m'
b = '\033[0;32m'
c = '\033[0;37m'
d = '\033[1;37m'

print(f'\n{d}Make sure you are not in Monitor mode!\n')
host = input(f'{d}wsf ({a}HOST{d})> {c}')
if host.lower() == 'back':
	quit()
else:
	print(f'{d}HOST => {b}{host}')

os.system(f'netdiscover -r {host}')
