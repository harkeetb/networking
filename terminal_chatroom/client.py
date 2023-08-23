#Harkeet Bal
#Client-side chat room

import socket
import threading

#define constants
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = 'utf-8'
BYTE_SIZE = 1024

#initialize client socket object, and connect to destination address
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((DEST_IP, DEST_PORT))

#function: sendMessage
#purpose: send a message to the server which will be broadcasted
def sendMessage():
    pass

#function receiveMessage
#purpose: receive an incoming message via server
def receiveMessage():
    pass
