import math

while True:
  try:
    wejscie = raw_input()
  except EOFError:
    break
  n = float(wejscie)
  sqrtdelta = math.sqrt(8*n-7)
  k1 = (-1-sqrtdelta)/2
  k2 = (-1+sqrtdelta)/2
  if k1 > 0:
    print int(math.ceil(k1))
  else:
    print int(math.ceil(k2))
