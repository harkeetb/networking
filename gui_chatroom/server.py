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
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

#Initialize two lists to store client sockets, and the names
client_socket_list = []
client_name_list = []

#function: broadcast_message
#params: message: message to be sent to clients connected to server
#purpose: broadcast a message to connected clients
def broadcast_message(message):
    for client_socket in client_socket_list:
        client_socket.send(message)         #should not need to encode here, since the message was already encoded prior to being passed as argument

#function: receive_message
#params: socket: incoming message from a client
#purpose: receive an incoming message from SPECIFIC client and forward message to be broadcast
def receive_message(client_socket):
    connected = True
    while connected:
        try:
            #Retrieve name of client socket from name list
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            #Receive message from the client
            message = client_socket.recv(BYTE_SIZE).decode(ENCODER)
            message =f"{name}: {message}".encode(ENCODER)
            broadcast_message(message)
        except:
            #Find the index of client socket in the lists
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            #Remove the client socket and name from lists
            client_socket_list.remove(client_socket)
            client_name_list.remove(name)

            #Close client socket
            client_socket.close()
            
            #Broadcast the client has been removed from the chat
            broadcast_message(f"{name} has left the chat.".encode(ENCODER))
            connected = False

#function: connect_client
#purpose: connect an incoming client to the server
def connect_client():
    connected = True    #boolean flag to determine whether to continue listening for clients

    while connected:
        #accept incoming client connection and print address of client
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}...")

        #send a name flag to prompt the connected client for their name
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTE_SIZE).decode(ENCODER)

        #append new client socket and client name to their appropriate lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        #send an update the server, individual client, and all clients regarding the new client connection
        print(f"Name of the new client is: {client_name}\n")     #server
        client_socket.send(f"{client_name}, you have connected to the server.".encode(ENCODER))   #individual client
        broadcast_message(f"{client_name} has joined the chat.".encode(ENCODER))  #all clients

        #Since a new client has connected, start a thread
        receive_thread = threading.Thread(target = receive_message, args=(client_socket,))
        receive_thread.start()

#Start server
print(f"Server is listening for incoming client connections at {HOST_IP}:{HOST_PORT}")
connect_client()
