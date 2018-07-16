from panda import Panda

panda = Panda()

raw_input("unplug ecu and press any key to start logging")

unplugged = []

try:
  while True:
    data = panda.can_recv()
    for addr, _, dat, bus in data:
      if hex(addr) not in unplugged:
        unplugged.append(hex(addr)) 
except KeyboardInterrupt:
  pass

raw_input("plug in ecu and press any key to start logging")

try:
  while True:
    data = panda.can_recv()
    for addr, _, dat, bus in data:
      if hex(addr) not in unplugged:
        print hex(addr)
        unplugged.append(hex(addr))
        print "found addr %s on bus %d"  % (str(hex(addr)), bus)
except KeyboardInterrupt:
  pass
