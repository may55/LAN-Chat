import socket
import sctp


HOST = '127.1.1.1'
PORT = 33000


sk=sctp.sctpsocket_tcp(socket.AF_INET)
sk.bind((HOST,PORT))
sk.listen(5)
print('listening.........')
conn,addr=sk.accept()
print('Recived',addr)
while True:
    data=conn.recv(1024)
    message = bytes('you got connection',"utf8")
    if not data:
        break
    conn.sendall(message)
sk.close()