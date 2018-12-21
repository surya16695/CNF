import socket
def main():
	host = '10.10.9.7'
	port = 4000

	soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	soc.bind((host, port))
	while True:
		data, addr = soc.recvfrom(1024)
		giventext = str(data.decode())
		print('Text from client : ' + giventext)
		data = giventext.upper()
		print('Sending : ' + str(data))
		soc.sendto(data.encode(), addr)
	soc.close()

if __name__ == '__main__':
	main()
