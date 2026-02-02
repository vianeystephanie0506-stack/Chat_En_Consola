import socket

HOST = "192.168.1.72"  # IP de tu máquina en la red local
PORT = 9090             # mismo puerto en cliente y servidor

# Crear el socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permite reutilizar el puerto rápidamente si reinicias el servidor
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Asociar IP y puerto
server_socket.bind((HOST, PORT))

# Escuchar conexiones
server_socket.listen(5)  # permite hasta 5 clientes en cola
print("Servidor escuchando en", HOST, "puerto", PORT)

try:
    while True:
        # Espera a que un cliente se conecte
        conn, addr = server_socket.accept()
        print(f"Conectado desde {addr}")

        # Manejo del cliente
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Cliente dice:", data.decode())
                conn.sendall(b"Mensaje recibido")
                
except KeyboardInterrupt:
    print("\nServidor detenido manualmente.")

finally:
    server_socket.close()
