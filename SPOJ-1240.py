t = int(raw_input())
while t > 0:
  wejscie = raw_input()
  punkty = wejscie.split()
  x1 = int(punkty[0])
  y1 = int(punkty[1])
  x2 = int(punkty[2])
  y2 = int(punkty[3])
  x3 = int(punkty[4])
  y3 = int(punkty[5])
  det = x1*y2 + x2*y3 + x3*y1 - x3*y2 - x2*y1 - x1*y3
  if det == 0:
    print 'TAK'
  else:
    print 'NIE'
  t -= 1
