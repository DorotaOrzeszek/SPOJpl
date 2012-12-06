sumawielokrotna = 0
while True:
  try:
    wejscie = raw_input()
  except EOFError:
    print sumawielokrotna
    break
  wejscie2 = wejscie.split()
  sumalinii = 0
  for liczba in wejscie2:
    sumalinii += int(liczba)
  print sumalinii
  sumawielokrotna += sumalinii
