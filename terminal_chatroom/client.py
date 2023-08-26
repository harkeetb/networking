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
    connected = True
    while connected:
        message = input("")
        clientSocket.send(message.encode(ENCODER))

#function receiveMessage
#purpose: receive an incoming message via server
def receiveMessage():
    connected = True

    while connected:
        try:
            #receive an incoming message from server
            message = clientSocket.recv(BYTE_SIZE).decode(ENCODER)

            #check for the name flag
            if message == "NAME":
                name = input("What is your name? ")
                clientSocket.send(name.encode(ENCODER))
            #else, print the message
            else:
                print(message)
        except:
            #an error occurred, close client connection
            print("Exception occurred.")
            clientSocket.close
            connected = False

#Create threads to continuously send and receive messages
sendThread = threading.Thread(target = sendMessage)
receiveThread = threading.Thread(target = receiveMessage)

#Start the client
sendThread.start()
receiveThread.start()