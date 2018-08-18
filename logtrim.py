#!/usr/bin/env python2

import sys

if len(sys.argv) != 4:
  print "usage: ./logprint.py log.csv <start time> <end time>"
  sys.exit()

start = float(sys.argv[2])
stop = float(sys.argv[3])
log = open(sys.argv[1]).readlines()
logg = log

with open(sys.argv[1].split(".csv")[0] + "_trimmed.csv", "w") as f:
  f.write(log[0])
  for i in range(1, len(log)):
    try:
      t = float(log[i].split(",")[0])
    except:
      continue
    if t >= start and t <= stop:
      f.write(log[i])
    elif t > stop:
      break
