t = input()
while t > 0:
  wejscie = raw_input()
  wejscie_split = wejscie.split()
  n = int(wejscie_split[0])
  k = int(wejscie_split[1])
  if k == 0 or k == n:
    kombinacje = 1
  elif k <= 0.5*n: 
    dzielnik = k
    for i in range(1,k):
      dzielnik *= i
    dzielna = n
    for i in range(n-k+1,n):
      dzielna *= i
    kombinacje = dzielna / dzielnik
  else:
    dzielnik = n-k
    for i in range(1,n-k):
      dzielnik *= i
    dzielna = n
    for i in range(k+1,n):
      dzielna *= i
    kombinacje = dzielna / dzielnik
  print kombinacje
  t -= 1
