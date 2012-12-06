while True:
  wejscie = raw_input()
  n = int(wejscie)
  if n == 0:
    break
  if n % 15 == 0:
    print 'TAK'
  else:
    print 'NIE'
