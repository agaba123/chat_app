import socket

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print('Connected to', HOST, 'on port', PORT)

    while True:
        message = input("Client: ")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print("Server: " + data)
        if data == "Closing connection...":
            break

    client_socket.close()
