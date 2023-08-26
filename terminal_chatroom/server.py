#Harkeet Bal
#Server-side chat room

#imports needed for program
import socket
import threading

#define constants
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345                                       #arbitrary port address
ENCODER = 'utf-8'
BYTE_SIZE = 1024

#Initialize server socket object using TCP, bind to host addresses, and listen for connections
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST_IP, HOST_PORT))
serverSocket.listen()

#Initialize two lists to store client sockets, and the names
clientSocketList = []
clientNameList = []

#function: broadcastMessage
#params: message: message to be sent to clients connected to server
#purpose: broadcast a message to connected clients
def broadcastMessage(message):
    pass

#function: receiveMessage
#params: socket: incoming message from a client
#purpose: receive an incoming message from SPECIFIC client and forward message to be broadcast
def receiveMessage(clientSocket):
    connected = True
    while connected:
        try:
            #Retrieve name of client socket from name list
            index = clientSocketList.index(clientSocket)
            name = clientNameList[index]

            #Receive message from the client
            message = clientSocket.recv(BYTE_SIZE).decode(ENCODER)
            message =f"{name}: {message}".encode(ENCODER)
            broadcastMessage(message)
        except:
            #Find the index of client socket in the lists
            index = clientSocketList.index(clientSocket)
            name = clientNameList[index]

            #Remove the client socket and name from lists
            clientSocketList.remove(clientSocket)
            clientNameList.remove(name)

            #Close client socket
            clientSocket.close()
            
            #Broadcast the client has been removed from the chat
            broadcastMessage(f"{name} has left the chat.".encode(ENCODER))
            connected = False

#function: connectClient
#purpose: connect an incoming client to the server
def connectClient():
    connected = True    #boolean flag to determine whether to continue listening for clients

    while connected:
        #accept incoming client connection and print address of client
        clientSocket, clientAddress = serverSocket.accept()
        print(f"Connected with {clientAddress}.")

        #send a name flag to prompt the connected client for their name
        clientSocket.send("NAME".encode(ENCODER))
        clientName = clientSocket.recv(BYTE_SIZE).decode(ENCODER)

        #append new client socket and client name to their appropriate lists
        clientSocketList.append(clientSocket)
        clientNameList.append(clientName)

        #send an update the server, individual client, and all clients regarding the new client connection
        print(f"Name of the new client is: {clientName}\n")     #server
        clientSocket.send(f"{clientName}, you have connected to the server.".encode(ENCODER))   #individual client
        broadcastMessage(f"{clientName} has joined the chat.".encode(ENCODER))  #all clients

        #Since a new client has connected, start a thread
        receiveThread = threading.Thread(target = receiveMessage, args=(clientSocket,))
        receiveThread.start()

#Start server
print("Server is listening for incoming client connections")
connectClient()