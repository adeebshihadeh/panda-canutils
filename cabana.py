# parse logs exported from cabana 


# string of bytes to list of bits
def get_bits(b):
  ret = []
  print(len(b))
  for i in range(0, len(b), 2):
    ret += list(bin(int(b[i:i+2], base=16))[2:].zfill(8))
  return ret


class Log:
  def __init__(self, csv):
    self.csv = csv
    
    csv = csv.split("\n")
    self.header = csv[0]
    self.data = csv[1:] 
  
    self.parsed = None

  def get_header(self):
    return self.header.split(",")

  # returns dict of addresses that appear in log
  # value is amount of occurences
  def get_addrs(self):
    log = self.get_full_log()
    ret = {}
    for msg in log:
      ret[msg[1]] = 1 + ret.get(msg[1], 0)
    return ret

  # list of msgs, each msg is a list of format:
  # [time, addr, bus, dat]
  def get_full_log(self):
    if self.parsed is not None: return self.parsed
    log = []
    for line in self.data:
      line = line.split(",")
      if len(line) != 4:
        continue
      time, addr, bus, dat = line
      log.append((float(time), int(addr), int(bus), dat))
    self.parsed = log
    return self.parsed 

  # optionally specify addrs, else return diff on all addrs
  def get_bit_diff(self, addrs=None):
    log = self.get_full_log()
    ret = {}
    for time, addr, bus, dat in log:
      if addrs is not None and addr not in addrs:
        continue
      bits = get_bits(dat)
      if addr not in ret:
        ret[addr] = bits
      else:
        for i, b in enumerate(bits):
          ret[addr][i] = '2' if ret[addr][i] != b else ret[addr][i]
    return ret

  def get_raw_lines(self):
    return self.csv.split("\n")


if __name__ == "__main__":
  test = ["88", "ff", "0000"]
  for t in test:
    print(t, get_bits(t))

  log = Log(open("data/pcm_cancel.csv").read())
  print(log.get_bit_diff())
