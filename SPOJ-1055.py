t = input()
while t > 0:
  wejscie = raw_input()
  wejscie2 = wejscie.split()
  ileliczb = int(wejscie2[0])
  liczby = wejscie2[1:]
  nieparzyste = liczby[::2]
  parzyste = liczby[1::2]
  print " ".join(parzyste), " ".join(nieparzyste)
  t -= 1
