#!/usr/bin/env python2.7

import sys

if __name__ == "__main__":
  if len(sys.argv) != 4:
    print "usage: {} log.csv <start time> <end time>".format(sys.argv[0])
    exit(-1)

  start = float(sys.argv[2])
  stop = float(sys.argv[3])
  log = open(sys.argv[1]).readlines()

  with open(sys.argv[1].split(".csv")[0] + "_trimmed.csv", "w") as f:
    f.write(log[0])
    for line in log[1:]:
      if len(line.split(",")) != 4:
        continue
      t = float(line.split(",")[0])
      if t >= start and t <= stop:
        f.write(line)
      elif t > stop:
        break

