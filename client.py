# Sends messages to the server
# Receiver messages from the server

# Required modules
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

HOST = "127.0.0.1"
PORT = 1234

# Creating a socket
# AF_INET: Using IPv4 addresses
# SOCK_STEAM: Using TCP packets for communication  
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Function that writes message on the message text box
def add_message(message):
    message_box.config(state=tk.NORMAL) # To insert message
    message_box.insert(tk.END, message + "\n")
    message_box.config(state=tk.DISABLED) # Cant insert message anymore

# Function to connect user to the chat
def connect():
    # Connect to the server
    try:
        client.connect((HOST, PORT))
        print(f"Successfully connected to server {HOST} on port {PORT}!")
        add_message("[SERVER] Successfully connected to the server!")
    except:
        messagebox.showerror("Unable to connect to server", f"ERROR! Unable connect to host: {HOST} on port: {PORT}")    

    username = username_textbox.get()
    if username != "":
        client.sendall(username.encode())
    else:
        messagebox.showerror("Invalid Username", "Your username cannot be empty")
        
    threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()

    # Disable the username text box and the join button after user has joined
    username_textbox.config(state=tk.DISABLED)
    username_button.config(state=tk.DISABLED)
    
# Function to send a message 
def send_message():
    message = message_textbox.get()
    if message != "":
        client.sendall(message.encode())
        message_textbox.delete(0, len(message)) # Clear the message text box after sending message
    else:
        messagebox.showerror("Empty Message", "Message cannot be empty")
        
# GUI
# Colours and font variables
FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 11)
BUTTON_FONT = ("Helvetica", 13)
LEMONADE = "#FCBACB"
BLUSH = "#FEC5E5"
STRAWBERRY = "#FC4C4E"
WHITE = "white"

root = tk.Tk() # Create the GUI window
root.geometry("600x600") # Pixel x Pixel
root.title("Talking to myself because I am lonely!")
root.resizable(False, False) # Not resizeable by width nor height

# Give a certain area to each row 
root.grid_rowconfigure(0, weight=1) # Top frame
root.grid_rowconfigure(1, weight=4) # Middle frame
root.grid_rowconfigure(2, weight=1) # Bottom frame

top_frame = tk.Frame(root, width=600, height=100, bg=LEMONADE)
top_frame.grid(row=0, column=0, sticky=tk.NSEW) 

middle_frame = tk.Frame(root, width=600, height=400, bg=BLUSH)
middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

bottom_frame = tk.Frame(root, width=600, height=100, bg=LEMONADE)
bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

username_label = tk.Label(top_frame, text="Enter Username:", font=FONT, bg=LEMONADE , fg=WHITE)
username_label.pack(side=tk.LEFT, padx=10)

username_textbox = tk.Entry(top_frame, font=FONT, bg=BLUSH, fg=WHITE, width=23)
username_textbox.pack(side=tk.LEFT)

username_button =tk.Button(top_frame, text="Join Chat", font=BUTTON_FONT, bg=STRAWBERRY, fg=WHITE, command=connect)
username_button.pack(side=tk.LEFT, padx=10)

message_textbox = tk.Entry(bottom_frame, font=FONT, bg=BLUSH, fg=WHITE, width=45)
message_textbox.pack(side=tk.LEFT, padx=10)

message_button = tk.Button(bottom_frame, text="SEND", font=BUTTON_FONT, bg=STRAWBERRY, fg=WHITE, command=send_message)
message_button.pack(side=tk.LEFT, padx=10)

message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=BLUSH, fg=WHITE, width=67, height=28)
message_box.config(state=tk.DISABLED) # Users will not be able to type inside the message text box
message_box.pack(side=tk.TOP)

# Function to listen all messages sent from the server and print it out
def listen_for_messages_from_server(client):
    while True:
        message = client.recv(2048).decode("utf-8")
        if message != "":
            username = message.split(":")[0]
            content = message.split(":")[1]

            add_message(f"[{username}]: {content}")
        else:
            messagebox.showerror("Error", "Message received from client is empty")

# Main function
def main():
    root.mainloop()

if __name__ == '__main__':
    main()  