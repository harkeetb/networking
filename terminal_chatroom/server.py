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
def receiveMessage(socket):
    pass

#function: connectClient
#purpose: connect an incoming client to the server
def connectClient():
    pass