import bluetooth as bt
import sys

print "Finding appropriate services..."

# we can filter the services found by address, uuid, and name of the service (rely on address and uuid because names
# can be volatile)
service_matches = bt.find_service()

if len(service_matches) == 0:
    print "Couldn't find any appropriate services"
    sys.exit(1)

# list out all matched services
# let user select from the list
for i in range(0, len(service_matches)):
    print "{}) {}".format(i, service_matches[i])

service_match_index = int(raw_input("Select a service: "))

service = service_matches[service_match_index]
port = service["port"]
server_address = service["host"]
name = service["name"]

print "Connecting to {} ({})".format(server_address, name)

# create client socket and connect to server
socket = bt.BluetoothSocket(bt.RFCOMM)
socket.connect((server_address, port))

print "Sending some data to the server..."

# send some data to server
socket.send('hello world!')

print "Sent data to the server"

print "Shutting down"

socket.close()
