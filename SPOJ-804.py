t = int(raw_input())
while t > 0:
  wejscie = raw_input()
  zetony = wejscie.split()
  a = int(zetony[0])
  b = int(zetony[1])
  while a != b:
    if a < b:
      b = b % a
      if b == 0:
        b = a
    if a > b:
      a = a % b
      if a == 0:
        a = b
  print a+b
  t -= 1
