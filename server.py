# Keep listening for any new client connections or messages
# Receive messages from client
# Send messages to other clients

# Required modules
import socket
import threading

HOST = "127.0.0.1" # Local host
PORT = 1234 # Any port from 0-65535
LISTENER_LIMIT = 3

# Main function
def main():
    # Creating the server socket
    # AF_INET: Using IPv4 addresses
    # SOCK_STEAM: Using TCP packets for communication 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind to that specific host and port
        server.bind((HOST, PORT))
        print(f"Running the server {HOST} on {PORT} ")
    except:
        print(f"ERROR! Unable to bind to host: {HOST} on port: {PORT}")

    # Set server limit of the amount of clients that can connect to the server
    server.listen(LISTENER_LIMIT)

    # Keep listening to client connections
    while True:
        client, address = server.accept()
        print(f"Successfully connected to client: {address[0]} {address[1]}")



# Only call the main function when server.py is runned
if __name__ == '__main__':
    main()