import socket
from datetime import datetime

# Server Configuration
HOST = '127.0.0.1'  
PORT = 65432        

HELP_MESSAGE = """
Welcome to the Simple Socket Server!

Available commands:
- time: returns the current server time.
- echo <message>: returns the <message> you send.
- exit: disconnects from the server.

Type your command:
"""

def handle_client(conn):
    # Send the help banner on connection
    conn.sendall(HELP_MESSAGE.encode('utf-8'))
    
    while True:
        # Receive data from the client
        data = conn.recv(1024).decode('utf-8').strip()
        if not data:
            break

        # Handle the 'time' command
        if data.lower() == 'time':
            response = str(datetime.now()) + '\n'

        # Handle the 'echo' command (e.g., "echo message")
        elif data.lower().startswith('echo'):
            message = data[5:]  # Get the message after "echo "
            response = message + '\n'

        # Handle the 'exit' command
        elif data.lower() == 'exit':
            response = "Goodbye!\n"
            conn.sendall(response.encode('utf-8'))
            break  # Disconnect the client

        # Unrecognized command
        else:
            response = HELP_MESSAGE + "Unknown command: " + data + '\n'

        # Send the response back to the client
        conn.sendall(response.encode('utf-8'))

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print(f"Server listening on {HOST}:{PORT}...")

    while True:
        # Accept a connection
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            handle_client(conn)
