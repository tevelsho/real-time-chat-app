# Keep listening for any new client connections or messages
# Receive messages from client
# Send messages to other clients

# Required modules
import socket
import threading

HOST = "127.0.0.1" # Local host
PORT = 1234 # Any port from 0-65535
LISTENER_LIMIT = 3
active_clients = [] # List of all currently connected users

# Function to listen for any incoming messages from connected clients
def listen_for_messages(client, username):
    while True:
        message = client.recv(2048).decode("utf-8")
        if message != "":
            final_msg = username + ":" + message
            send_messages_to_all(final_msg) 
        else:
            print(f"Message sent from {username} is empty.")

# Function to send message to a single connected client
def send_message_to_client(client, message):
    client.sendall(message.encode()) # Encode the message for encryption

# Function to send any new message to all the clients that are connected to the server
def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)

# Function to handle client
def client_handler(client):
    # Server listening for client message containing username
    while True:
        username = client.recv(2048).decode("utf-8")
        if username != "":
            active_clients.append((username, client))
            prompt_message = "SERVER:" + f"{username}" + "added to the chat" 
            send_messages_to_all(prompt_message)
            break;
        else:
            print("Client does not have a username!")

    threading.Thread(target=listen_for_messages(client, username, )).start()



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

        # Every time a client connects, the thread will start
        threading.Thread(target=client_handler, args=(client, )).start()

# Only call the main function when server.py is runned
if __name__ == '__main__':
    main()