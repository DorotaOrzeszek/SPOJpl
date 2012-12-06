while True:
  try:
    wejscie = raw_input()
  except EOFError:
    break
  szyfr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C']
  odp = ''
  for znak in wejscie:
    if znak == ' ':
      odp = odp + znak
    else:
      indeks = szyfr.index(znak)
      odp = odp + szyfr[indeks + 3]
  print odp
