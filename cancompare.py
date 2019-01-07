#!/usr/bin/env python2.7

# compare two can logs exported from cabana

import sys
from itertools import izip_longest
from cabana import Log

def safe_hex(a):
  return a if not isinstance(a, (int, long)) else hex(a)

# compare the addrs between two logs
def addr_diff(log1, log2):
  for bus in  [0, 1, 2, 128, 129, 130]:
    addrs1 = sorted(log1.get_addrs_on_bus(bus).keys())
    addrs2 = sorted(log2.get_addrs_on_bus(bus).keys())

    shared = [int(i) for i in addrs1 if i in addrs2]
    addrs1 = [int(i) for i in addrs1 if i not in shared]
    addrs2 = [int(i) for i in addrs2 if i not in shared]

    # dont print if no msgs on bus
    if not(len(shared) or len(addrs1) or len(addrs2)): continue

    print "*"*10, "bus", bus, "*"*10
    print len(shared), "shared"
    print len(addrs1), "only in log1"
    print len(addrs2), "only in log2"

    print "-"*20, "\nshared\tlog1\tlog2\n", "-"*20
    for s, l1, l2 in izip_longest(shared, addrs1, addrs2, fillvalue=""):
      print safe_hex(s), "\t", safe_hex(l1), "\t", safe_hex(l2)

# only outputs diff on addresses that appear in both logs
def bit_diff(log1, log2):
  diff1 = log1.get_bit_diff()
  diff2 = log2.get_bit_diff()

  for addr, bits in sorted(diff1.iteritems()):
    if addr not in diff2:
      continue

    diff = []
    for i, b in enumerate(bits):
      if b != diff2[addr][i]: diff.append(str(i))
    if len(diff):
      print "diff on addr", hex(addr), "\n\tbits", ", ".join(diff)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "usage: python cancompare.py <log 1> <log 2>"
    print "\nlogs are exported from cabana"
    print "add --bits arg at the end to run a diff on the bits instead of the addresses"
    print "add --bus arg at the end to differentiate betwween bus in addr mode"
    exit(-1)

  log1 = Log(open(sys.argv[1]).read())
  log2 = Log(open(sys.argv[2]).read())

  if "--bits" in sys.argv:
    bit_diff(log1, log2)
  else:
    addr_diff(log1, log2)

