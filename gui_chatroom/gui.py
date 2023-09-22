import tkinter
from tkinter import BOTH, END, DISABLED

#define root window
root = tkinter.Tk()
root.title("Chatroom")
root.geometry('600x600')
root.resizable(0,0)         #disable window resizing

#define colours
root_color = '#535657'
input_color = '#4f646f'
output_color = "#dee7e7"
root.config(bg=root_color)

#define font
text_font = ("Helvetica", 14)
black = "#000"
white = "#fff"

#define GUI layout:

#define frames
input_frame = tkinter.Frame(root, bg=input_color)
output_frame = tkinter.Frame(root, bg=output_color)
info_frame = tkinter.Frame(root, bg=input_color)
input_frame.pack()
output_frame.pack(pady=10)  #fill output frame both vertically and horizontally
info_frame.pack()

#info frame layout
name_label = tkinter.Label(info_frame, text="Client name:", font=text_font, fg=black, bg = input_color)
name_entry = tkinter.Entry(info_frame, borderwidth=3, font=text_font)
ip_label = tkinter.Label(info_frame, text="Host IP:", font=text_font, fg=black, bg=input_color)
ip_entry = tkinter.Entry(info_frame, borderwidth=3, font=text_font)
port_label = tkinter.Label(info_frame, text="Port #:", font=text_font, fg=black, bg=input_color)
port_entry = tkinter.Entry(info_frame, borderwidth=3, font=text_font, width=10)
connect_button = tkinter.Button(info_frame, text="Connect", font=text_font, bg=input_color, borderwidth=5, width=10)
disconnect_button = tkinter.Button(info_frame, text="Disconnect", font=text_font, bg=input_color, borderwidth=5,width=10, state=DISABLED)

name_label.grid(row=0, column=0, padx=2, pady=10)
name_entry.grid(row=0, column=1, padx=2, pady=10)
ip_label.grid(row=1, column=0, padx=2, pady=10)
ip_entry.grid(row=1, column=1, padx=2, pady=10)
port_label.grid(row=0, column=2, padx=2, pady=10)
port_entry.grid(row=0, column=3, padx=2, pady=10)
connect_button.grid(row=1, column=2, padx=4, pady=5)
disconnect_button.grid(row=1, column=3, padx=4, pady=5)

#define widgets 


#define functions:
#send user's typed message to the output frame
def send():
    message_label = tkinter.Label(output_frame, text=message_entry.get(), fg=black, bg=output_color,font=text_font)
    message_label.pack()

    #clear entry field
    message_entry.delete(0,END)


#root window main loop
root.mainloop()