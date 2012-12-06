t = input()
wejscie = []
while t > 0:
  wiersz = raw_input()
  wejscie.append(wiersz)  
  t -= 1
tekst = " ".join(wejscie)
litery = map(chr, range(97, 123))+map(chr, range(65, 91))
for litera in litery:
  powtorzenia = tekst.count(litera)
  if powtorzenia > 0:
    print litera, powtorzenia
