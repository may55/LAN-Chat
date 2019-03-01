#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        # print(list(client_address)[1])
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    user_list[name]=client
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
<<<<<<< HEAD
       
=======
        # print(addresses)
>>>>>>> ba149a934cd7c706345ecc4980d08a473e330f7f
        msg = client.recv(BUFSIZ)
        print(msg)
        if msg != bytes("{quit}", "utf8"):
<<<<<<< HEAD

=======
            msg1 = msg.decode("utf8")
            if(msg1[0]=='{'):
                print("hehuhu")
                user = ""
                left_msg = ""
                for i in range(1,len(msg)):
                    if(msg1[i]=='}'):
                        left_msg = msg1[i+1:]
                        break
                    else:
                        user += msg1[i]
                prefix = bytes(user + " : ", "utf8")
                if(user in user_list):
                    user_list[user].send(prefix+bytes(left_msg,"utf8"))
                else:
                    print(user+" user not present")
>>>>>>> ba149a934cd7c706345ecc4980d08a473e330f7f
            else:
                broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            print("%s has left the chat." %clients[client])
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
# print(clients)
addresses = {}
user_list={}

<<<<<<< HEAD

=======
HOST = ''
>>>>>>> ba149a934cd7c706345ecc4980d08a473e330f7f
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()