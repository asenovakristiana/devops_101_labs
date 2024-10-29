import socket
import struct

# Client configurations
HOST = '127.0.0.1'
PORT = 65432

# Define message types
MESSAGE_TYPE_HELLO = 1
MESSAGE_TYPE_GOODBYE = 2

# Send a binary message to the server
def send_message(sock, message_type, payload):
    payload_bytes = payload.encode()
    message_length = len(payload_bytes)
    
    # Pack length, type, and payload into binary format
    message = struct.pack('!IB', message_length, message_type) + payload_bytes
    escaped_message = ''.join(f'\\x{byte:02x}' for byte in message)
    print("Binary message in escaped format:", escaped_message)
    sock.sendall(message)

# Start client
def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("Connected to server.")
        
        # Send HELLO message
        send_message(client_socket, MESSAGE_TYPE_HELLO, "Hello, server!")

if __name__ == "__main__":
    start_client()