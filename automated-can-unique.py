import os, sys

def log(filename):
  raw_input("press any key to start recording")
  os.system("python can_logger.py") 
  os.system("mv output.csv " + filename)

print "background recording..."
log("background.csv")

try:
  while True:
    log("output.csv")
    os.system("python can_unique.py output.csv background.csv")
    os.remove("output.csv")
except KeyboardInterrupt:
  os.remove("background.csv")

