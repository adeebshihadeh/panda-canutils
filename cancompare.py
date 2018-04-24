import sys
from itertools import izip_longest

# ignores bus num

def can_compare(log1, log2):
  shared = []

  log1 = log1[1:]
  log1 = [l.split(",")[1] for l in log1 if len(l.split(",")) == 4]
  log1 = list(set(log1))
  log2 = log2[1:]
  log2 = [l.split(",")[1] for l in log2 if len(l.split(",")) == 4]
  log2 = list(set(log2))

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
    print "{0}\t{1}\t{2}".format(s, l1, l2)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "usage: python cancompare.py <log 1> <log 2>"
    print "\texport csv files from cabana"
    print "\twarning: cancompare ignores bus number"
    sys.exit()

  csv1 = open(sys.argv[1]).readlines()
  csv2 = open(sys.argv[2]).readlines()
  can_compare(csv1, csv2)
