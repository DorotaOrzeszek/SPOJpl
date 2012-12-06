while True:
  try:
    wejscie = raw_input()
  except EOFError:
    break
  wejscie2 = wejscie.split()
  j = int(wejscie2[0])
  wejscie3 = []
  for element in wejscie2[1:]:
    wejscie3.append(int(element))
  liczby = set(wejscie3)
  liczbybezpowtorzen = list(liczby)
  liczbybezpowtorzen.sort(None,None,True)
  try:
    odp = liczbybezpowtorzen[j-1]
    print int(odp)
  except IndexError:
    print '-'
