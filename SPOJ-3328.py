liczby = [] # list of ints

while True:
  try:
    wejscie = int(raw_input())
    liczby.append(wejscie)
  except EOFError:
    break

ilosci = {} # dictionary -> int: int
max = 0 # int

for liczba in liczby: # int in ints list
  ilosc = liczby.count(liczba) # int
  ilosci[liczba] = ilosc 
  if ilosc > max:
    max = ilosc
  
for liczba in ilosci:
  current = ilosci[liczba]
  newvalue = int(round(30 * current / float(max)))
  ilosci[liczba] = newvalue*'*'

# ilosci -> dictionary of strs

for i in range(-10,11): # int
  try:
    print str(i).rjust(4)+':|'+ilosci[i].ljust(30)+'|'#+'\n'
  except KeyError:
    print str(i).rjust(4)+':|'+''.ljust(30)+'|'#+'\n'
