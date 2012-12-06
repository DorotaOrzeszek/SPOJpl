while True:
  try:
    wejscie = raw_input()
  except EOFError:
    break
  wejscie2 = wejscie.split()
  ileliczb = 0
  ileslow = 0
  for element in wejscie2:
    try:
      int(element)
    except ValueError:
      ileslow += 1
      continue
    ileliczb += 1
  print ileliczb, ileslow
