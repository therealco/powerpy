import socket
import random
class TCPServer:
    def __init__(self, host='0.0.0.0', port=random.randint(1, 10000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

    def start(self):
        while True:
            # Accept a new connection
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address} has been established.")

            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Received: {data}")

            # Send a response to the client
            response = "Hello from server"
            client_socket.send(response.encode('utf-8'))
            print("Response sent")

            # Close the connection
            client_socket.close()

    def stop(self):
        self.server_socket.close()

if __name__ == "__main__":
    server = TCPServer(port=random.randint(1, 10000)
    try:
        server.start()
    except KeyboardInterrupt:
        print("Server is shutting down.")
        server.stop()
