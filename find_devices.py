# finds nearby available bluetooth devices

import bluetooth as bt

print "Searching for nearby devices"

nearby_devices = bt.discover_devices()

for address in nearby_devices:
    name = bt.lookup_name(address)
    if name is None:
        print "{} found".format(address)
    else:
        print "{} found: {}".format(address, name)
