#!/usr/bin/python
#tcpclient.py
#

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 1000)
print >>sys.stderr, 'starting up on %s port %s' % server_address

try:
	sock.connect(server_address)

	print >>sys.stderr, 'TCP Connection Success.'
	
	# Send data
	data = "DATA from Client"
	print >>sys.stderr, 'sending "%s"' % data
	sock.sendall(data)

	# Look for the response
	amount_received = 0
	amount_expected = len(data)
	
	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
		print >>sys.stderr, 'Received from Server "%s"' % data

except: 
	print >> sys.stderr, 'Failed to connect to %s port %s' % server_address
	print >>sys.stderr, 'closing socket'
	sock.close()
raw_input("Press Enter to continue...")