import socket
import os

FILES_DIRECTORY = './uploads/'

server_port = 7777

def receive_file():
    global server_port
    server_ip = '0.0.0.0'  # Listen on all interfaces
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print(f"Listening for incoming files on {server_ip}:{server_port}")

    connection, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    # Receiving the file
    with open(os.path.join(FILES_DIRECTORY, 'capture_result.pcap'), 'wb') as f:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            f.write(data)


        # Clean up the connection
    connection.close()
    server_socket.close()
    if server_port == 7777:
        server_port += 1
    elif server_port == 7778:
        server_port -= 1
    print("Socket closed.")

if __name__ == '__main__':
    while True:
        print("Start packet capturing...")
        receive_file()
