#Harkeet Bal
#Client Chatroom GUI
 
import tkinter
from tkinter import BOTH, END, DISABLED, VERTICAL

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
connect_button = tkinter.Button(info_frame, text="Connect", font=text_font, bg=input_color, borderwidth=0, width=10)
disconnect_button = tkinter.Button(info_frame, text="Disconnect", font=text_font, bg=input_color, borderwidth=0,width=10, state=DISABLED)

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
send_button = tkinter.Button(input_frame, text="Send", borderwidth=5, width=10, font=text_font, bg=input_color, state = DISABLED)

input_entry.grid(row=0, column=0, padx=5, pady=5)
send_button.grid(row=0, column=1, padx=5, pady=5)

#output frame layout
sbar = tkinter.Scrollbar(output_frame, orient=VERTICAL)
listbox = tkinter.Listbox(output_frame, height=22, width=60, borderwidth=3, bg = black, fg = output_color, font = text_font, yscrollcommand=sbar.set)
sbar.config(command=listbox.yview)

listbox.grid(row=0,column=0)
sbar.grid(row=0,column=1, sticky="NS")

#root window main loop
root.mainloop()