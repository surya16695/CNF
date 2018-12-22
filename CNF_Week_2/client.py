import socket
import threading

def main():
	host = '10.2.136.85'
	port = 8014
	soc = socket.socket()
	soc.connect((host, port))
	msg = soc.recv(1024).decode()
	print(msg)
	username = input()+''
	soc.send(username.encode())
	threading.Thread(target = username, args = (soc, username)).start()
	message = ''
	while message != 'q':
		msgs = soc.recv(1024).decode()
		print ('msgs')
		message = input()
		soc.send(message.encode())
	soc.close()

if __name__ == '__main__':
	main()
	