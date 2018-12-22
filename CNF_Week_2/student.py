import socket
import sys
import csv
import threading
from _thread import *
def clientthread(c, addr):

	f = open ('data.csv')
	stu_reader = csv.reader(f, delimiter = ',')
	line_count = 0
	student = []
	questions = []
	answers = []
	for row in stu_reader:
		student.append(row[0])
		print(student)
		questions.append(row[1])
		answers.append(row[2])

	while True:
		c.send('Enter your roll number :'.encode())
		username = c.recv(1024).decode()
		try:
			for student in students:
				if username == student:
					i = student.index()
					c.send('Secret question is : '.encode())
					c.send(questions[i].encode())
					ans = c.recv(1024).decode()
					try:
						answers[i] = ans
						c.send('Attendance success'.encode())
						print('Attendance success')
					except:
						c.send('Attendance failure'.encode())
						print('Attendance failure')
		except:
			c.send('ROLLNUMBER-NOTFOUND'.encode())
	c.close()

host = '10.2.136.85'
port = 8014
soc = socket.socket()
soc.bind((host, port))
soc.listen(1)
print('server is ready')
while True:
    c, addr = soc.accept()
    print('connected from  ' + str(addr))
    start_new_thread(clientthread, (c, addr))
s.close()


