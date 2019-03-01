import socket

HOST = ''
PORT = 1520

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen()
	conn,addr = s.accept()
	# print(conn)
	with conn:
		print('Recived ', addr)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(data)