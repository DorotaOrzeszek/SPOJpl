litery = map(chr, range(97,123)) + map(chr, range(65,91))

def kodowanie(litera): # litera -> str
  if ord(litera) in range(97,110):
    szyfr = chr(ord(litera)+13)
  elif ord(litera) in range(110,123):
    szyfr = chr(97+ord(litera)-110)
  elif ord(litera) in range(65,78):
    szyfr = chr(ord(litera)+13)
  elif ord(litera) in range(78,91):
    szyfr = chr(65+ord(litera)-78)
  elif ord(litera) in range(48,53):
    szyfr = chr(ord(litera)+5)
  elif ord(litera) in range(53,58):
    szyfr = chr(ord(litera)-5)
  else:
    szyfr = litera
  return szyfr
  
while True:
  try:
    wejscie = raw_input()
  except EOFError:
    break
  wyjscie = ''
  for char in wejscie:
    wyjscie += kodowanie(char)
  print wyjscie
