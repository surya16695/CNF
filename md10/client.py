import socket
import sys
import select
host = '192.168.137.1'
port = 2000
server = socket.socket()
server.connect((host, port))
# data = s.recv(2048)
# message = input("-->")
# while message != 'x':
# 	s.send(message.encode())
# 	data = s.recv(2048)
# 	print('other:- ' + str(data.decode()))
# 	message = input("-->")
# s.close()
while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print(message)
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
