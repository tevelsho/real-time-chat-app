This Python-based chat application provides real-time communication between multiple clients through a server. The server and client scripts use sockets for communication and feature a graphical user interface (GUI) built using the tkinter library.

Modules Used

    socket: Enables communication between the server and clients over a network.
    threading: Allows for concurrent execution of multiple tasks, such as listening for incoming messages and handling client connections.
    tkinter: Provides the GUI framework for creating the client interface, including text entry fields, buttons, and message display.

Usage Instructions

    Start the server by running server.py. The server will listen for incoming connections from clients.
    Connect to the server by running client.py. Enter a username and click "Join Chat" to connect. (You can start multiple clients to talk to each other)
    Start sending and receiving messages in real-time with other connected clients.

Note: Ensure the server is running and accessible before connecting with the client application.
Important Points

    The server script (server.py) handles incoming client connections and messages, broadcasting messages to all connected clients.
    The client script (client.py) connects to the server, sends and receives messages, and updates the GUI with incoming messages.
    Messages are transmitted as UTF-8 encoded strings over the network.
    The client GUI includes entry fields for username and message input, as well as a message display area for viewing conversation history.

Dependencies

    Python 3.x
    tkinter library (usually comes pre-installed with Python)
