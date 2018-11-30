#!/usr/bin/env python3
# python ssl socket test client
# The server receives client data encrypted by TLSv01?
# Server and client keeps TCP/IP connection open until closed by client
# By Per Dahsltroem pda@ucl.dk
# 30-11-2018
import socket, ssl       # Fetch the socket module

HOST = '192.168.1.10'  # Standard loopback interface address
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
DataCommingIn = True

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind((HOST, PORT))
mySocket.listen()
print('Awaiting connection on IP: ',mySocket.getsockname()[0],\
                          ' Port: ',mySocket.getsockname()[1])
connectionSocket, fromAddress = mySocket.accept() # Wait and create connection object
print('Connection from:', fromAddress)
mySSLSocket = ssl.wrap_socket(connectionSocket,
                             server_side=True,
                             certfile="serverCertificate.crt",
                             keyfile="serverPrivate.key")
while DataCommingIn:
    receivedData = mySSLSocket.recv(16)
    print(receivedData.decode('utf-8'))
    if not receivedData:
        DataCommingIn = False
mySSLSocket.close()
print('Connection closed')
mySocket.close()
print('Socket closed')