import math
t = int(raw_input())

while t > 0:
  n = input()
  punkty = []
  for i in range(0,n):
    wejscie = raw_input()
    nazwa = wejscie.split()[0]
    x = int(wejscie.split()[1])
    y = int(wejscie.split()[2])
    odleglosc = math.sqrt(x**2+y**2)
    punkt = (odleglosc,nazwa,x,y)
    punkty.append(punkt)
  raw_input()
  punkty.sort()
  for element in punkty:
    print element[1]+" "+str(element[2])+" "+str(element[3])
  print
  t -= 1
