import socket
import sctp
HOST=''
PORT=6556

sk=sctp.sctpsocket_tcp(socket.AF_INET)

sk.connect((HOST,PORT))
message=bytes('Message',"utf-8")
sk.sendall(message)
data=sk.recv(1024)
print(data)
