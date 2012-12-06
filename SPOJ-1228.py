wejscie = raw_input()
wejscie2 = wejscie.split()
a = float(wejscie2[0])
b = float(wejscie2[1])
c = float(wejscie2[2])
# ax + b = c do postaci ax + b' = 0
# czyli b' = b-c
if a == 0 and b-c == 0:
  print 'NWR'
elif a == 0 and b-c != 0:
  print 'BR'
else:
  odp = -(b-c) / a
  print '%0.2f' % odp
