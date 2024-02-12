# Sends messages to the server
# Receiver messages from the server

# Required modules
import socket
import threading

HOST = "127.0.0.1"
PORT = 1234

def main():
    # Creating a socket 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    try:
        client.connect((HOST, PORT))
        print(f"Successfully connected to server {HOST} on port {PORT}!")
    except:
        print(f"ERROR! Unable connect to host: {HOST} on port: {PORT}")

if __name__ == '__main__':
    main()






