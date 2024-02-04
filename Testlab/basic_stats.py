import math
def average(n):
  s = 0
  for i in range(0,len(n)):
    s += n[i]
  return s/len(n)

def std(n):
  avg = average(n)
  s = 0
  for i in range(len(n)):
    s += math.pow(n[i]-avg,2)
  return math.sqrt(s/len(n))