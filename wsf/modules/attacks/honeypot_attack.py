# wifisploit/modules/honeypot_attack.py

import socket
import threading
import chardet
import platform
import os

a = '\033[0;31m'
b = '\033[0;32m'
c = '\033[0;37m'
d = '\033[1;37m'

host = input(f'{d}wsf ({a}HOST{d})> {c}')
if host.lower() == 'back':
	quit()
else:
	print(f'{d}HOST => {b}{host}')

port = 23
def handle_client(conn, addr):
	print(f'{c}Connected by', addr)
	conn.sendall(b'Successfully login to Windows 10 23h2!\n')
	while True:
		conn.sendall(b'telnet> ')
		data = conn.recv(1024)
		if not data:
			break
		result = chardet.detect(data)
		encoding = result['encoding']

		try:
			data = data.decode(encoding)
			print(f'{addr} Try command: {data}')

		except UnicodedecodeError:
			print('Failed to decode data!')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((host, port))
	s.listen()
	while True:
		conn, addr = s.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
