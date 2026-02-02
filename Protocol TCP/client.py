import socket

HOST = "192.168.1.68"  # IP del servidor
PORT = 9090

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))  # solo connect, nada de bind()

print("Conectado al servidor. Escribe tus mensajes. Para salir, escribe 'salir'.")

try:
    while True:
        mensaje = input("Tú: ")
        if mensaje.lower() == "salir":
            break
        client_socket.sendall(mensaje.encode())
        data = client_socket.recv(1024)
        print("Servidor responde:", data.decode())

finally:
    client_socket.close()
    print("Conexión cerrada.")
