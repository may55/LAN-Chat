import socket
import sctp
HOST='127.0.0.8'
PORT=6556

sk=sctp.sctpsocket_tcp(socket.AF_INET)

sk.connect((HOST,PORT))
message=bytes('Message',"utf-8")
sk.sendall(message)
data=sk.recv(1024)
print(data)
