l1 = int(raw_input())
for n in range(100):
  ln = l1 - n
  if (ln % 3 == 0) and (ln % 5 == 0):
    print 'SPOKOKOKO'
  elif (ln % 3 == 0):
    print 'KOKO'
  elif (ln % 5 == 0):
    print 'SPOKO'
  else:
    print ln
