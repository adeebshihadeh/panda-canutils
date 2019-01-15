#!/usr/bin/env python3

# get addrs where specified value occurs throughout whole log in same byte

import sys
from cabana import Log

def findbyte(log, byte):
  full_log = log.get_full_log()
  addrs = {k: 0 for k in log.get_addrs().keys()}

  for t, addr, bus, dat in full_log:
    if addrs[addr] == []: continue
    if addrs[addr] == 0: addrs[addr] = []

    bs = []
    for i in range(0, len(dat), 2):
      if int(dat[i:i+2], 16) == byte:
        bs.append(i)
    if len(addrs[addr]) == 0:
      addrs[addr] = bs
    else:
      addrs[addr] = [b for b in bs if b in addrs[addr]]
  ret = sorted([a for a in addrs.keys() if len(addrs[a]) > 0])
  return [hex(a) for a in ret]


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("usage: {} log.csv 0xFF")
    exit(-1)

  log = Log(open(sys.argv[1]).read())
  print(findbyte(log, int(sys.argv[2], 0)))

