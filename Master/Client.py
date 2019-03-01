import socket

HOST = ''
PORT = 6556

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST,PORT))
	message = bytes('Message',"utf8")
	s.sendall(message)
	data = s.recv(1024)

print('Asish bhai is saying', data.decode("utf8"))