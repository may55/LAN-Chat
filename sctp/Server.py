import socket
import sctp

HOST = '127.0.0.8'
PORT = 6556

sk=sctp.sctpsocket_tcp(socket.AF_INET)
sk.bind((HOST,PORT))
sk.listen()
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