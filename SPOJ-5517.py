import math

wejscie = raw_input()
okrag = wejscie.split()
x0 = int(okrag[0])
y0 = int(okrag[1])
r = int(okrag[2])
n = int(raw_input())
while n > 0:
  wejscie2 = raw_input()
  punkt = wejscie2.split()
  x1 = int(punkt[0])
  y1 = int(punkt[1])
  d = math.sqrt((x1-x0)**2+(y1-y0)**2)
  if d < r:
    print 'I'
  elif d > r:
    print 'O'
  else:
    print 'E' 
  n -= 1
