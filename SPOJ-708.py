def collatz(s):
  wyniki = []
  wyniki.append(s)
  n = 1
  while wyniki[-1] != 1:
    if wyniki[n-1] % 2 == 0: 
      wyniki.append(wyniki[n-1]/2.0)
    else:
      wyniki.append(wyniki[n-1]*3.0+1)
    n += 1
  print n-1

t = int(raw_input())
while t > 0:
  s = int(raw_input())
  collatz(s)
  t -= 1
