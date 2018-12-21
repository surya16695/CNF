import socket
import threading
from _thread import *
from threading import *
import os
import signal
import time
def check():
	if(active_count() == 2):
		time.sleep(15)
		if(active_count() == 2):
			os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)

def clientthread(conn, addr):
	while True:
		try:
			message = conn.recv(2048)
			for client in client_list:
				if client != conn:
					client.send(message)
		except:
			client_list.remove(conn)
			status = client_dict[conn] + ' is disconnected'
			for client in client_list:
				if(client != conn):
					client.send(status.encode())
			check()
			return 1
	conn.close()

host = '10.10.9.7'
port = 2000
s = socket.socket()
s.bind((host, port))
print('server is ready')
s.listen(10)
client_list = []
client_dict = {}
while True:
	conn, addr = s.accept()
	client_list.append(conn)
	print(str(addr) + ' connected:')
	conn.send('welcome to avengerschat'.encode())
	conn.send('enter username'.encode())
	username = conn.recv(1024).decode()
	client_dict[conn] = username
	Thread(target = clientthread,args = (conn,addr)).start()
conn.close()
s.close()






