import socket

HOST = "192.168.0.67"  # IP del servidor
PORT = 8080        # mismo puerto que el servidor

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.sendall(b"Hola servidor")

data = client_socket.recv(1024)
print("Servidor responde:", data.decode())

client_socket.close()
