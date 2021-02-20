import socket 
#selectors is a more abstract module than select 
import selectors

# default selectors differe depending on the OS 
selector = selectors.DefaultSelector()

#init the server
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 1337))
    server_socket.listen()
    #add the server socket into the watchlist
    selector.register(server_socket, selectors.EVENT_READ, accept_connections)

def accept_connections(server_socket):
    client_socket, addr = server_socket.accept()
    print("Connection established with: ", addr)
    selector.register(client_socket, selectors.EVENT_READ, send_message)

def send_message(client_socket):
    request = client_socket.recv(4094)
    if request:
        response = 'Hi there \n '.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()

def event_loop():
    while True:

        events = selector.select()
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)

if __name__ == '__main__':
    server()
    event_loop()
