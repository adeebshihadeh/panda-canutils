from panda import Panda

panda = Panda()

raw_input("unplug ecu and press any key to start logging")

unplugged = []

try:
  while True:
    data = panda.can_recv()
    for msg in data:
      if list(msg)[0] not in unplugged:
        unplugged.append(list(msg)[0]) 
except KeyboardInterrupt:
  pass

raw_input("plug in ecu and press any key to start logging")

try:
  while True:
   for msg in panda.can_recv():
    if list(msg)[0] not in unplugged:
      print list(msg)
      unplugged.append(list(msg)[0])
      #print "found addr: %s on bus: %d"  % (list(msg)[0], list(msg)[4])
except KeyboardInterrupt:
  pass
