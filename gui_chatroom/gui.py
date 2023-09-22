import tkinter
from tkinter import BOTH, END

#define root window
root = tkinter.Tk()
root.title("Chatroom")
root.geometry('400x600')
root.resizable(0,0)         #disable window resizing

#define colours
root_color = '#535657'
input_color = '#4f646f'
output_color = "#dee7e7"
root.config(bg=root_color)

#define GUI layout:

#define frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH, expand=True)  #fill output frame both vertically and horizontally

#define functions:

#send user's typed message to the output frame
def send():
    message_label = tkinter.Label(output_frame, text=message_entry.get(), fg='#000', bg=output_color, font=("Helvetica", 12))
    message_label.pack()

    #clear entry field
    message_entry.delete(0,END)

#define widgets
message_entry = tkinter.Entry(input_frame, text="Enter message", width=20, font=("Helvetica", 12))
send_button = tkinter.Button(input_frame, text="Send", bg=output_color, command=send)                      
message_entry.grid(row=0, column=0, padx=10, pady=10)                   
send_button.grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=5)

#root window main loop
root.mainloop()