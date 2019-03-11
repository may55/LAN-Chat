import socket
import sctp
HOST='192.168.1.1'
PORT=33001

sk=sctp.sctpsocket_tcp(socket.AF_INET)

sk.connect((HOST,PORT))
message=bytes('Message',"utf-8")
sk.sendall(message)
data=sk.recv(1024)
print(data)
