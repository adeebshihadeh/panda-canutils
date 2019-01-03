#!/usr/bin/env python3

# get a bit diff on a specific addr

import sys
from cabana import Log 

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("usage: {} log.csv addr1 addr2".format(sys.argv[0]))
    print("example: {} log.csv 0x343 0x98".format(sys.argv[0]))
    exit(0)

  log = Log(open(sys.argv[1]).read())
  addrs = [int(n, 0) for n in sys.argv[2:]]

  diff = log.get_bit_diff(addrs)
  
  for k, v in diff.items():
    print(hex(k))
    for i in range(0, len(v), 8):
      print("\t"  + str(v[i:i+8]))
