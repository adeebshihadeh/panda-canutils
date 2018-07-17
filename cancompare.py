#!/usr/bin/env python2

import sys
from binascii import hexlify
from itertools import izip_longest

def get_bits(b):
  ret = []

  for i in xrange(0, len(b), 2):
    ret += list(bin(int(b[i:i+2], base=16))[2:].zfill(8))

  return ret

def id_diff(log1, log2):
  log1 = log1[1:]
  log1 = [l.split(",")[1] for l in log1 if len(l.split(",")) == 4]
  log1 = list(set(log1))
  log2 = log2[1:]
  log2 = [l.split(",")[1] for l in log2 if len(l.split(",")) == 4]
  log2 = list(set(log2))


  shared = list()
  shared = [i for i in log1 if i in log2]
  log1 = [i for i in log1 if i not in shared]
  log2 = [i for i in log2 if i not in shared]

  print len(shared), "shared"
  print len(log1), "only in log 1"
  print len(log2), "only in log 2"

  print "-"*20
  print "shared\tlog1\tlog2"
  print "-"*20

  for s, l1, l2 in izip_longest(shared, log1, log2):
    print "{}\t{}\t{}".format("" if not s else hex(int(s)), "" if l1 is None else hex(int(l1)), "" if not l2 else hex(int(l2)))

def bit_diff(log1, log2, save):
  seen = []

  for log in (log1, log2):
    messages = {}
    for line in log[1:]:
      line = line.strip().split(",")[1:]

      if len(line) == 3:
        addr, _, b = line

        if addr not in messages:
          messages[addr] = get_bits(b)
        else:
          bits = get_bits(b)
          for i in range(len(bits)):
            if messages[addr][i] != 2:
              messages[addr][i] = 2 if messages[addr][i] != bits[i] else bits[i]
    seen.append(dict(sorted(messages.items())))

  for addr in seen[0]:
    if addr not in seen[1]:
      continue

    bits = []
    for i in range(len(seen[0][addr])):
      if seen[0][addr][i] != seen[1][addr][i]:
        bits.append(str(i + 1))
    if len(bits):
      print "diff on addr", hex(int(addr)), "\n   bits", ', '.join(bits)

  if save:
    with open("output", "w") as f:
      for log in seen:
        f.write("{0} log {0}\n".format("="*10))
        for addr in log:
          f.write("\t{}\n".format(hex(int(addr))))
          for i in range(len(log[addr])/8):
            f.write("\t\t{}\n".format(" ".join(map(str, log[addr][i*8:i*8+8]))))



if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "usage: python cancompare.py <log 1> <log 2>"
    print "\nlogs are exported from cabana"
    print "add --bits arg at the end to run a diff on the bits instead of the ids"
    print "add --save arg at the end to save the bit data for every message to an output file"
    print "**warning** cancompare ignores bus number"
    sys.exit()

  csv1 = open(sys.argv[1]).readlines()
  csv2 = open(sys.argv[2]).readlines()
  if "--bits" in sys.argv:
    bit_diff(csv1, csv2, "--save" in sys.argv)
  else:
    id_diff(csv1, csv2)
