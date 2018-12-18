import socket

def Main():
    host = '127.0.0.1'
    port = 5001
    server = ('127.0.0.1', 5000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    message = input("->")
    while message != 'q':
        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        data = data.decode()
        print("received from server " + str(data))
        message = input("->")
    s.close()
if __name__ == '__main__':
    Main()