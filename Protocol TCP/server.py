import socket

HOST = "127.0.0.1"  # localhost
PORT = 65432        # puerto (no privilegiado)

# Crear el socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asociar IP y puerto
server_socket.bind((HOST, PORT))

# Escuchar conexiones (máx 1 en cola)
server_socket.listen(1)

print("Servidor escuchando...")

conn, addr = server_socket.accept()
print(f"Conectado desde {addr}")

with conn:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Cliente dice:", data.decode())
        conn.sendall(b"Mensaje recibido")

server_socket.close()
