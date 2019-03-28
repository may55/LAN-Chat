import socket 
import sctp
from threading import Thread

def accept_incoming_connections():
	while True:
		client,client_add = s.accept()
		print("%s : %s has connected." %client_add)
		client.send(bytes("Enter name of the user :","utf8"))
		address[client] = client_add
		Thread(target=handle_client,args=(client,)).start()


def handle_client(client):

	name = client.recv(BUFFSIZE).decode("utf8")
	client.send(bytes("Welcome %s Type {quit} to quit." %name,"utf8"))
	clients[client] = name
	while True:
		msg = client.recv(BUFFSIZE)
		print(msg)
		if(msg!=bytes("{quit}","utf8")):
			msg_decoded = msg.decode("utf8")
			if(msg_decoded[0]=='{'):
				user,left_msg = msg_decoded.split('}')
				user = user[1:]
				left_msg = left_msg.strip()

				prefix = bytes(name+" : ","utf8")

				if(user in user_list):
					user_list[user].send(prefix+bytes(left_msg,"utf8"))
					client.send(prefix+bytes(left_msg,"utf8"))
				else:
					print(user + "user not present")
			else:
				broadcast(msg,name+" : ")
		else:
			client.close()
			del clients[client]
			broadcast(bytes("%s has left the chat." %name,"utf8"))

def broadcast(msg,prefix=""):
	for sock in clients:
		sock.send(bytes(prefix,"utf8")+msg)


HOST = '192.168.100.5'
PORT = 33000
BUFFSIZE = 1024
ADD = (HOST,PORT)

clients = {}
address = {}
user_list = {}



s = sctp.sctpsocket_tcp(socket.AF_INET)
s.bind(ADD)

s.listen(5)
print("Listen for Connection")
thread = Thread(target=accept_incoming_connections)
thread.start()
thread.join()
s.close()

# sk.listen(5)
# print('listening.........')
# conn,addr=sk.accept()
# print('Recived',addr)
# while True:
#     data=conn.recv(1024)
#     message = bytes('you got connection',"utf8")
#     if not data:
#         break
#     conn.sendall(message)
# sk.close()
