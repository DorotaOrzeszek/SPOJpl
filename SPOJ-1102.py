import math

t = input()
while t > 0:
  wejscie = raw_input()
  wejscie2 = wejscie.split()
  liczby = wejscie2[1:]
  n = float(wejscie2[0])
  count = 0
  for element in liczby:
    count += float(element)
  srednia = count / n
  mindelta = 101
  for element in liczby:
    delta = math.fabs(float(element)-srednia)
    if delta < mindelta:
      mindelta = delta
      minelement = element
  print minelement
  t -= 1
