wymiary = raw_input()
wymiary2 = wymiary.split()
rzedy = int(wymiary2[0])
kolumny = int(wymiary2[1])
macierz = []
k = 0
while k < rzedy:
  wejscie = raw_input()
  rzad = wejscie.split()
  macierz.append(rzad)
  k += 1
for i in range(0,kolumny):
  for j in range(0,rzedy):
    print macierz[j][i],
  print 
