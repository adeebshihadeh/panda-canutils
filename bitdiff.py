#!/usr/bin/env python3

# get a bit diff on a specific addr

import sys
from cabana import Log

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("usage: {} log.csv addr1 addr2".format(sys.argv[0]))
    print("default bus is 0. specify different bus with --bus bus_num")
    print("example: {} log.csv --bus 0 0x343 0x2e4".format(sys.argv[0]))
    exit(0)

  log = Log(open(sys.argv[1]).read())
a:
  bus = 0
  if "--bus" in sys.argv:
    bus = int(sys.argv.pop(sys.argv.index("--bus")+1))
    sys.argv.pop(sys.argv.index("--bus"))
  addrs = [int(n, 0) for n in sys.argv[2:]]

  diff = log.get_bit_diff_on_bus(addrs, bus=bus)
  for k, v in diff.items():
    print(hex(k))
    for i in range(0, len(v), 8):
      print("\t"  + str([int(n) for n in v[i:i+8]]))
