import socket 

#creating a tcp server socket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind(('localhost', 1337))
ss.listen()

while True:
    #listening to incoming connections
    client_socket, addr = ss.accept()
    print('Connections Established with: ', client_socket, addr)
    #once the connection has been made we can now proccess it
    while True:
        request = client_socket.recv(4096)
        print(request)
        if not request:
            break
        else:
            response = 'Hello wolrd \n '.encode()
            client_socket.send(response)


    #good practice to close connections
    client_socket.close()

#The problem is that we cant really have more than 1 connection at a time