t = input()
while t > 0:
  wejscie = raw_input()
  n = int(wejscie.split()[0])
  x = int(wejscie.split()[1])
  y = int(wejscie.split()[2])
  odp = []
  for liczba in range(2,n):
    if liczba % x == 0 and liczba % y != 0:
      odp.append(str(liczba))
  wyjscie = " ".join(odp) 
  print wyjscie
  t -= 1
