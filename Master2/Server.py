#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        print(clients)
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            # "{ashi2} HEllo bhai kesa h"
            if(msg==bytes("{ashi2} HEllo bhai kesa h", "utf8")):
                user = "ashi2"
                prefix = ""
                left_message = '{ashi2} HEllo bhai kesa h'
                for sock in clients:
                    if clients[sock]=="ashi2":
                        sock.send(bytes(prefix, "utf8")+left_message)
                        break;
                # for i in range(1,len(msg)):
                #     if(msg[i]=='}'):
                #         left_message = msg[i+1:]
                #         break
                #     else:
                #         user += msg[i]
                # if(user in clients):
                # user.send(bytes(prefix, "utf8")+left_message)
                # else:
                #     print("User not present")
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
addresses = {}

HOST = '127.0.0.1'
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