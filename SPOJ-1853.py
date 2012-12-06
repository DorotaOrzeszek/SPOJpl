while True:
  try:
    wejscie = raw_input()
  except EOFError:
    break
  if len(wejscie) == 0:
    continue
  dane = wejscie.split()
  if len(dane) != 7:
    print 3
    continue
  imie = dane[1][:-1]
  nazwisko = dane[3][:-1]
  data = dane[6].split('-')
  odp = 100
  if not imie.istitle():
    odp = 0
    print odp
    continue
  else:# imie.istitle():
    broken = False
    for char in imie[1:]:
      if char not in map(chr, range(97, 123)):
        odp = 0
        print odp
        broken = True
        break
    if broken:
      continue
  if not nazwisko.istitle():
    odp = 1
    print odp
    continue
  else:# nazwisko.istitle():
    broken = False
    for char in nazwisko[1:]:
      if char not in map(chr, range(97, 123)):
        odp = 1
        print odp
        broken = True
        break
      if broken:
        continue

  if len(data) != 3:
    print 2
    continue
  try:
    rok = int(data[0])
    miesiac = int(data[1])
    dzien = int(data[2])
  except ValueError:
    print 2
    continue
  if rok not in range(1900,2001):
    odp = 2
    print odp
    continue
  elif miesiac not in range(1,13):
    odp = 2
    print odp
    continue
  elif dzien not in range(1,32):
    odp = 2
    print odp
    continue

  if odp == 100:
    odp = 3
    print odp
