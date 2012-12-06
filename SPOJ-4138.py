t = int(raw_input())
while t > 0:
  wejscie = raw_input()
  wejscie2 = wejscie.split()
  c = int(wejscie2[0])
  k = int(wejscie2[1])
  w = int(wejscie2[2])
  if c*w <= k:
    print 'yes'
  else:
    print 'no'
  t -= 1
