# Sends messages to the server
# Receiver messages from the server

# Required modules
import socket
import threading

HOST = "127.0.0.1"
PORT = 1234

# Function to listen all messages sent from the server and print it out
def listen_for_messages_from_server(client):
    while True:
        message = client.recv(2048).decode("utf-8")
        if message != "":
            username = message.split(":")[0]
            content = message.split(":")[1]

            print(f"[{username}]: {content}")
            print("")
        else:
            print("Message received from client is empty")

# Funtion to send the encoded message to the server
def send_message_to_server(client):
    while True:
        message = input("Message: ")
        if message != "":
            client.sendall(message.encode())
        else:
            print("Empty message")
            exit(0)

# Function to prompt user for their username and send it over to the server
def communicate_to_server(client):
    username = input("Enter your username: ")
    print("")
    if username != "":
        client.sendall(username.encode())
    else:
        print("Your username cannot be empty")
        exit(0)

    threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()

    send_message_to_server(client)

def main():
    # Creating a socket
    # AF_INET: Using IPv4 addresses
    # SOCK_STEAM: Using TCP packets for communication  
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    try:
        client.connect((HOST, PORT))
        print(f"Successfully connected to server {HOST} on port {PORT}!")
    except:
        print(f"ERROR! Unable connect to host: {HOST} on port: {PORT}")

    communicate_to_server(client)




if __name__ == '__main__':
    main()






