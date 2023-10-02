#Harkeet Bal
#Client-side w/ GUI 

#imports
import socket
import threading
import tkinter

#constants
ENCODER = 'utf-8'
BYTE_SIZE = 1024

#define functions:
##################

#function: connect
#purpose: connect to a server at it's given IP/Port address
def connect():
    global client_socket

    #clear previous chats
    listbox.delete(0,tkinter.END)

    #retrieve connection parameters
    name = name_entry.get()
    ip = ip_entry.get()
    port = port_entry.get()

    #check that all required parameters were received
    if name and ip and port:
        listbox.insert(0, f"{name} is waiting to connect to {ip} at {port}.")

        #create client socket and connect to server using TCP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, int(port)))
        
        #verify connection to server
        verify(name)
    else:
        #required params were missing
        listbox.insert(0, "Insufficient information, unable to connect.")
    
#function: verify
#purpose: ensure that the server connection is valid
def verify(name):
    global client_socket
    
    # The server will send a NAME flag if a valid connection is made
    flag = client_socket.recv(1024).decode(ENCODER)

    if flag == 'NAME':
        # the connection was made, send client name and await verification
        client_socket.send(name.encode(ENCODER))
        message = client_socket.recv(BYTE_SIZE).decode(ENCODER)

        if message:
            # server sent a verification, so connection is valid
            listbox.insert(0, message)
            
            # update entry states (for buttons)
            connect_button.config(state=tkinter.DISABLED)
            disconnect_button.config(state=tkinter.NORMAL)
            send_button.config(state=tkinter.NORMAL)
            name_entry.config(state=tkinter.DISABLED)
            ip_entry.config(state=tkinter.DISABLED)
            port_entry.config(state=tkinter.DISABLED)

            # create a thread to continuously receive messages from server
            receive_thread = threading.Thread(target=receive_message)
            receive_thread.start()
        else:
            # no verification message was received
            listbox.insert(0, "Connection not verified")
            client_socket.close()
    else:
        # no name flag was sent, connection was refused
        listbox.insert(0, "Connection refused")
        client_socket.close()


#function: disconnect
#purpose: disconnect from the chat server
def disconnect():
    global client_socket

    # close the socket
    client_socket.close()

    # update entry states (for buttons)
    connect_button.config(state=tkinter.NORMAL)
    disconnect_button.config(state=tkinter.DISABLED)
    send_button.config(state=tkinter.DISABLED)
    name_entry.config(state=tkinter.NORMAL)
    ip_entry.config(state=tkinter.NORMAL)
    port_entry.config(state=tkinter.NORMAL)

#function: send_message
#purpose send a message to the chat server
def send_message():
    global client_socket

    # send the message to server
    message = input_entry.get()
    client_socket.send(message.encode(ENCODER))

    # clear input entry
    input_entry.delete(0, tkinter.END)

#function: receive
#purpose: send receive a message from the chat server
def receive_message():
    global client_socket
    connected = True

    while connected:
        try:
            # receive an incoming message from the server
            message = client_socket.recv(BYTE_SIZE).decode(ENCODER)
            listbox.insert(0,message)
        except:
            # an error occurred, so disconnect from server
            listbox.insert(0, "Closing the connection")
            disconnect()
            connected = False

#Tkinter GUI definition:
########################

#define root window
root = tkinter.Tk()
root.title("Chatroom")
root.geometry('600x600')
root.resizable(0,0)         #disable window resizing

#define colors and font
root_color = '#535657'
input_color = '#4f646f'
output_color = "#dee7e7"
root.config(bg=root_color)
text_font = ("Helvetica", 14)
black = "#000"

#define GUI layout:

#define frames
input_frame = tkinter.Frame(root, bg=input_color)
output_frame = tkinter.Frame(root, bg=output_color)
info_frame = tkinter.Frame(root, bg=input_color)
input_frame.pack(pady=10)
output_frame.pack(pady=10)
info_frame.pack(pady=10)

#info frame layout
name_label = tkinter.Label(info_frame, text="Client name:", font=text_font, fg=black, bg = input_color)
name_entry = tkinter.Entry(info_frame, borderwidth=3, font=text_font)
ip_label = tkinter.Label(info_frame, text="Host IP:", font=text_font, fg=black, bg=input_color)
ip_entry = tkinter.Entry(info_frame, borderwidth=3, font=text_font)
port_label = tkinter.Label(info_frame, text="Port #:", font=text_font, fg=black, bg=input_color)
port_entry = tkinter.Entry(info_frame, borderwidth=3, font=text_font, width=10)
connect_button = tkinter.Button(info_frame, text="Connect", font=text_font, bg=input_color, borderwidth=0, width=10, command=connect)
disconnect_button = tkinter.Button(info_frame, text="Disconnect", font=text_font, bg=input_color, borderwidth=0,width=10, state=tkinter.DISABLED, command=disconnect)

name_label.grid(row=0, column=0, padx=2, pady=10)
name_entry.grid(row=0, column=1, padx=2, pady=10)
ip_label.grid(row=1, column=0, padx=2, pady=5)
ip_entry.grid(row=1, column=1, padx=2, pady=5)
port_label.grid(row=0, column=2, padx=2, pady=10)
port_entry.grid(row=0, column=3, padx=2, pady=10)
connect_button.grid(row=1, column=2, padx=4, pady=5)
disconnect_button.grid(row=1, column=3, padx=4, pady=5)

#input frame layout
input_entry = tkinter.Entry(input_frame, width=45, borderwidth=3, font=text_font)
send_button = tkinter.Button(input_frame, text="Send", borderwidth=5, width=10, font=text_font, bg=input_color, state = tkinter.DISABLED, command=send_message)

input_entry.grid(row=0, column=0, padx=5, pady=5)
send_button.grid(row=0, column=1, padx=5, pady=5)

#output frame layout
sbar = tkinter.Scrollbar(output_frame, orient=tkinter.VERTICAL)
listbox = tkinter.Listbox(output_frame, height=22, width=60, borderwidth=3, bg = black, fg = output_color, font = text_font, yscrollcommand=sbar.set)
sbar.config(command=listbox.yview)

listbox.grid(row=0,column=0)
sbar.grid(row=0,column=1, sticky="NS")


#run root window
root.mainloop()