#!/usr/bin/python
#tcpserver.py

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('0.0.0.0', 1000)
print >>sys.stderr, 'starting up on %s port %s' % server_address

# Bind to address, port
sock.bind(server_address)

# Listen on socket
sock.listen(1)

while True:
	# Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            if data:
                print >>sys.stderr, 'Received from Client : "%s"' % data
                serverData = "DATA from Server"
                print >>sys.stderr, 'Sending to Client : "%s"' % serverData
                connection.sendall(serverData)
            else:
                break
            
    finally:
        # Clean up the connection
        connection.close()
raw_input("Press Enter to continue...")