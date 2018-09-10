#!/usr/bin/env python2.7

# find bytes
# for matching same messages with different id's across different model cars

import sys
from collections import OrderedDict

def findbyte(val, loc, log):
  # ignore header
  log = log[1:]

  found = {}
  for l in log:
    l = l.strip().split(",")

    if len(l) != 4: continue

    b = int(l[3][loc*2-2:loc*2], 16)

    if b == val:
      addr = int(l[1])
      if addr not in found:
        found[addr] = 1
      else:
        found[addr] += 1

  return sorted(((v, k) for (k, v) in found.items()), reverse=True)


if __name__ == "__main__":

  if len(sys.argv) != 5:
    print "usage ./findbit.py <csv file> <byte val> <byte location> <threshold>"
    print "byte location is 1-8"
    print "threshold is min occurences to print an addr out"
    print "export csv files from cabana"
    sys.exit(0)

  log = open(sys.argv[1]).readlines()
  val = int(sys.argv[2], 10 if "0x" not in sys.argv[2] else 16)
  threshold = int(sys.argv[4])

  found = findbyte(val, int(sys.argv[3]), log)
  for n, addr in found:
    if n < threshold:
      break
    print hex(addr), n

