import socket 
#select is a system fucntion that monitors file-objects
from select import select

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 1337))
server_socket.listen()

def accept_connections(server_socket):
    client_socket, addr = server_socket.accept()
    print("Connection established with: ", addr)

    #once that connection is made we can now send it to the watchlist
    to_monitor.append(client_socket)

def send_message(client_socket):
    request = client_socket.recv(4094)
    if request:
        response = 'Hi there \n '.encode()
        client_socket.send(response)
    else:
        client_socket.close()

def event_loop():
    while True:
        #select function takes 3 lists of files as args 
        #files ready to read, ready to write, errors
        #We only will be needing ready to read files
        ready_to_read, _, _, = select(to_monitor, [], [])

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connections(sock)
            else:
                send_message(sock)

if '__name__' == '__main__':
    to_monitor.append(server_socket)
    event_loop()
