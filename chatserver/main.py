import socket

HOST = ''
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))

    server_socket.listen(1)

    conn, addr = server_socket.accept()

    print('Connected by', addr)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Client: " + data)
        if data == "bye":
            conn.send("Closing connection...".encode())
            break
        message = input("Server: ")
        conn.send(message.encode())

    conn.close()
