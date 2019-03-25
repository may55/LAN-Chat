import socket
import sctp
<<<<<<< HEAD
HOST='192.168.1.1'
PORT=33001
=======
HOST=''
PORT=6556
>>>>>>> 8933f29cba04f2705125999e221615617a7541ed

sk=sctp.sctpsocket_tcp(socket.AF_INET)

sk.connect((HOST,PORT))
message=bytes('Message',"utf-8")
sk.sendall(message)
data=sk.recv(1024)
print(data)
