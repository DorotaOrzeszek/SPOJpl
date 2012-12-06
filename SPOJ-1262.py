wejscie = raw_input()
wejscie1 = wejscie.split()
n = int(wejscie1[0])
k = int(wejscie1[1])
wejscie2 = raw_input()
liczby = wejscie2.split()
rolled = liczby[k:] + liczby[:k]
for element in rolled:
  print int(element),
