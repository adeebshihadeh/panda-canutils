# detect single bit changes

from panda import Panda
import binascii

panda = Panda()

raw_input("press any key to start background logging")

msgs = {}

def get_bits(bytes):
  return list(bin(int(binascii.hexlify(bytes), base=16)).zfill(len(binascii.hexlify(bytes)*8)))

try:
  while True:
    data = panda.can_recv()

    for addr, _, dat, src in data:
      bits = get_bits(dat)
      if addr not in msgs[src]:
        msgs[src][addr] = bits
      else:
        for bit in msgs[src][addr]:
          bit = 2 if bit != bits.pop(0) else bit
except KeyboardInterrupt:
  pass

raw_input("press any key to start logging again")

try:
  while True:
    data = panda.can_recv()

    for addr, _, dat, src in data:
      bits = get_bits(dat)
      for i in range(len(dat)):
        if msgs[src][addr][i] != 2 and msgs[src][addr][i] != bits.pop(0): 
          msgs[src][addr][i] = 2
          print "addr " + str(addr) + " bus " + " bit " + str(i) 
except KeyboardInterrupt:
  pass
