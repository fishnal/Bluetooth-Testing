import bluetooth as bt
from PyOBEX.client import Client
from PIL import Image
import sys

print "Finding appropriate services..."

if len(sys.argv) > 1:
	addr = sys.argv[1]
	if len(sys.argv) > 2:
		service_name = sys.argv[2]
	else:
		service_name = None
else:
	addr = None
	service_name = None

# we can filter the services found by address, uuid, and name of the service (rely on address and uuid because names
# can be volatile)
service_matches = bt.find_service(name=service_name, address=addr)

if len(service_matches) == 0:
    print "Couldn't find any appropriate services"
    sys.exit(1)

# list out all matched services
# let user select from the list
for i in range(0, len(service_matches)):
    print"{}) {}".format(i, service_matches[i])

service_match_index = int(raw_input("Select a service: "))

service = service_matches[service_match_index]
port = service["port"]
server_address = service["host"]
name = service["name"]

# connect to server
print "Connecting to {} ({})".format(name, server_address)
client = Client(server_address, port)
client.connect()

# send some file
print "Sending a file..."
f = open("c:/users/vpxbo/desktop/test_image.jpg", 'rb')
client.put("test.jpg", f.read())

# disconnect from server
print "Disconnecting..."
client.disconnect()

print "Done"