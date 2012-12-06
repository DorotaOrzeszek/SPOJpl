licznik = 0
while True:
  try:
    plik = raw_input()
    licznik += 1
  except EOFError:
    break
print licznik
