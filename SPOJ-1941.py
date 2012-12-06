while True:
  try:
    wejscie = raw_input()
  except EOFError:
    break
  
  dane = wejscie.split()
  a = int(dane[0])
  znak = dane[1]
  b = int(dane[2])
  if znak == '==':
    if a == b:
      print 1
    else:
      print 0
  if znak == '!=':
    if a != b:
      print 1
    else:
      print 0
  if znak == '<=':
    if a <= b:
      print 1
    else:
      print 0
  if znak == '>=':  
    if a >= b:
      print 1
    else:
      print 0
