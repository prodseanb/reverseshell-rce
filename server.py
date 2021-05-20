import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1' #loopback, will be the server's ip
port = 1234 #port we're tunneling data into 

#bind server
server.bind((host,port))
server.listen(5)

run = True
client, addr = server.accept()
print('Connection opened: ', addr) 

while run:
	try:
		data = input('>>>')
		client.send('Trojan Infected.'.encode('UTF-8')) #Send to client
		msg = client.recv(1024) #receive from client 
		print(msg.decode('UTF-8'))
	except ConnectionResetError:
		print('Client lost. Retrying...')
		client, addr = server.accept()
		print('Connection opened: ', addr)