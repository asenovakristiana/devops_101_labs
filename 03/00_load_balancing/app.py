import socket
import argparse

def create_server(name, host='127.0.0.1', port=8080):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Serving HTTP on {host}:{port}")
    print(f"Server name set to: {name}")

    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive the request
        request_data = client_socket.recv(1024).decode('utf-8')
        print("Request received:")
        print(request_data)

        # Check if the request is a GET request
        if request_data.startswith("GET"):
            # Create a simple HTTP response
            response = "HTTP/1.1 200 OK\n"
            response += "Content-Type: text/html\n\n"
            response += f"<html><body><h1>Hello from {name}!</h1></body></html>"
        else:
            # Handle other HTTP methods (e.g., POST) with a 405 Method Not Allowed
            response = "HTTP/1.1 405 Method Not Allowed\n\n"

        # Send the response to the client
        client_socket.sendall(response.encode('utf-8'))

        # Close the connection
        client_socket.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python HTTP Server with custom port and name.")
    parser.add_argument("--port", type=int, default=8080, help="Port to bind the HTTP server (default: 8080)")
    parser.add_argument("--name", type=str, default="server", help="Name to display in the HTML response")

    args = parser.parse_args()
    create_server(name=args.name, port=args.port)