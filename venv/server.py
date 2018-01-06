import bluetooth as bt

print "Starting server. Waiting for a client socket to accept"

# create server socket, bind to some host and port, let server socket listen
server_socket = bt.BluetoothSocket(bt.RFCOMM)
server_socket.bind(("", bt.PORT_ANY))
server_socket.listen(backlog=1)

# advertise a service with a given name, set of service classes, and profiles
# for our case, try to limit this to serial port or obex object push (or whatever else the devices can support)z
bt.advertise_service(server_socket,
                     "OBEX Object Push",
                     service_classes=[bt.OBEX_OBJPUSH_CLASS],
                     profiles=[bt.OBEX_OBJPUSH_PROFILE])

# let server socket accept client connectioon
client_socket, client_info = server_socket.accept()
print "Accepted connection from ", client_info

# receive data from client and print it
data = client_socket.recv(1024)
print "Received [%s]", data

print "Closing connection"

client_socket.close()
client_info.close()
