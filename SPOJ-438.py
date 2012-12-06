liczby = [False,False]+(9999)*[True]
for j in range(2,101):
  if liczby[j]:
    for i in range(2*j,10001,j):
      liczby[i] = False

t = int(raw_input())
while t > 0:
  m = int(raw_input())
  if not liczby[m]:
    print 'NIE'
  else:
    print 'TAK'
  t -= 1
