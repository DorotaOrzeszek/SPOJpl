n = int(raw_input())
liczby = []
while n > 0:
  x = int(raw_input())
  liczby.append(x)
  n -= 1
wejscie = raw_input()
warunek = wejscie.split()
if warunek[0] == '<':
  for liczba in liczby:
    if liczba < int(warunek[1]):
      print liczba
else:
  for liczba in liczby:
    if liczba > int(warunek[1]):
      print liczba
