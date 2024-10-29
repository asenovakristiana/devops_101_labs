import socket
import struct

# Server configurations
HOST = '127.0.0.1'
PORT = 65432

# Define message types
MESSAGE_TYPE_HELLO = 1
MESSAGE_TYPE_GOODBYE = 2

# Start server
def start_server():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            server_socket.listen()
            print("Server listening on:", HOST, PORT)
            
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    # Read message length and type
                    header = conn.recv(5)  # 4 bytes length + 1 byte type
                    if not header:
                        break
                    
                    # Unpack header
                    message_length, message_type = struct.unpack('!IB', header)
                    
                    # Read the payload based on the length received
                    payload = conn.recv(message_length)
                    
                    if message_type == MESSAGE_TYPE_HELLO:
                        print("Received HELLO message:", payload.decode())
                    else:
                        break

if __name__ == "__main__":
    start_server()