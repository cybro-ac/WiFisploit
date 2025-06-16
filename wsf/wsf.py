# python3

import os

a = '\033[0;31m'
b = '\033[0;32m'
c = '\033[0;37m'
d = '\033[1;37m'

print(f'''{b}

             ::    .'|.  ::                  '||           ::    .   
... ... ... .... .||.   ....  ....  ... ...   ||    ...   .... .||.  
 ||  ||  |   ||   ||     ||  ||. '   ||'  ||  ||  .|  '|.  ||   ||   
  ||| |||    ||   ||     ||  . '|.   ||    |  ||  ||   ||  ||   ||   
   |   |    .||. .||.   .||. |'..|'  ||...'  .||.  '|..|' .||.  '|.' 
                                     ||                              
                                    .||.
Developed by Cybaron AC
''')
while True:
	try:
		cmd = input(f'\n{d}wsf> {c}')
		if not cmd:
			continue
		if cmd.lower() == 'help':
			print(f'''
{b}wifisploit{c} from Cybaron AC.

#   COMMAND:					DESCRIPTION:

0   help					Display help menu.
1   clear					Clean terminal screen.
2   ifconfig					Display network interface settings.
3   iwconfig					Display wireless network interfaces settings.
4   kill					Prepare your wireless adapter.
5   start					Start monitor mode.
6   stop					Stop monitor mode.
7   modules				 	Display all modules.
8   tutorial					Tool tutorial.
9   install					Install requirements.
10  exit					Leave the tool.

There is 12 {b}moudles{c} you can use!
			''')
		elif cmd.lower() == 'clear':
			os.system('clear')

		elif cmd.lower() == 'ifconfig':
			os.system('ifconfig')

		elif cmd.lower() == 'iwconfig':
			os.system('iwconfig')

		elif cmd.lower() == 'kill':
			os.system('airmon-ng check kill')
			os.system('systemctl restart NetworkManager')

		elif cmd.startswith('start '):
			os.system(f'airmon-ng start {cmd[6:]}')

		elif cmd.startswith('stop '):
			os.system(f'airmon-ng stop {cmd[5:]}')

		elif cmd.lower() == 'modules':
			print(f'''
#   MODULE:					DESCRIPTION:

0   modules/scanners/scan_all			Scanning all networks.
1   modules/scanners/scan_net			Scanning single network.
2   modules/scanners/scan_wash			Scanning with wash.
3   modules/scanners/scan_wps			Scanning WPS networks.
4   modules/scanners/net_discover		Scanning with netdiscover.
5   modules/captures/capture_traffic	  	Capturing traffics on network.
6   modules/captures/capture_handshake		Capturing 4-way handshake.
7   modules/attacks/brute_force			WiFi brute-force without wordlist.
8   modules/attacks/crack_handshake		Cracking handshake with wordlist.
9   modules/attacks/dos_attack			Network Denial of Service attack.
10  modules/attacks/wps_attack			Start WPS PIN attack.
11  modules/attacks/honeypot_attack		Start Honeypot attack.

Type {b}use <MODULE>{c} or {b}use <#>{c}, example {b}use honeypot_attack{c} or {b}use 11{c}.
			''')

		elif cmd.lower() == 'use scan_all' or cmd.lower() == 'use 0':
			os.system('python3 modules/scanners/scan_all.py')

		elif cmd.lower() == 'use scan_net' or cmd.lower() == 'use 1':
			os.system('python3 modules/scanners/scan_net.py')

		elif cmd.lower() == 'use scan_wash' or cmd.lower() == 'use 2':
                        os.system('python3 modules/scanners/scan_wash.py')

		elif cmd.lower() == 'use scan_wps' or cmd.lower() == 'use 3':
                        os.system('python3 modules/scanners/scan_wps.py')

		elif cmd.lower() == 'use net_discover' or cmd.lower() == 'use 4':
                        os.system('python3 modules/scanners/net_discover.py')

		elif cmd.lower() == 'use capture_traffic' or cmd.lower() == 'use 5':
			os.system('python3 modules/captures/capture_traffic.py')

		elif cmd.lower() == 'use capture_handshake' or cmd.lower() == 'use 6':
			os.system('python3 modules/captures/capture_handshake.py')

		elif cmd.lower() == 'use brute_force' or cmd.lower() == 'use 7':
			os.system('python3 modules/attacks/brute_force.py')

		elif cmd.lower() == 'use crack_handshake' or cmd.lower() == 'use 8':
			os.system('python3 modules/attacks/crack_handshake.py')

		elif cmd.lower() == 'use dos_attack' or cmd.lower() == 'use 9':
			os.system('python3 modules/attacks/dos_attack.py')

		elif cmd.lower() == 'use wps_attack' or cmd.lower() == 'use 10':
			os.system('python3 modules/attacks/wps_attack.py')

		elif cmd.lower() == 'use honeypot_attack' or cmd.lower() == 'use 11':
			os.system('python3 modules/attacks/honeypot_attack.py')

		elif cmd.lower() == 'tutorial':
			os.system('xdg-open https://www.youtube.com/@cybaron_ac/featured')

		elif cmd.lower() == 'install':
			os.system('apt update -y && apt upgrade -y')
			os.system('apt install xterm -y')
			os.system('apt install mdk4 -y')

		elif cmd.lower() == 'exit':
			quit()

		else:
			print(f"{a}No such command '{cmd}'.")

	except Exception:
		print('{a}Syntax Error!')
