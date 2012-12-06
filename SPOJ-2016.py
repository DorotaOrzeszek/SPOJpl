wejscie = ''
newLines = 0
while True:
  try:
    wejscie1 = raw_input()
    wejscie += wejscie1
    newLines += 1
  except EOFError:
    break
wyjscie = 256*[0]
for char in wejscie:
  wyjscie[ord(char)] += 1
wyjscie[10] += newLines
for i in range(0,256):
  if wyjscie[i] != 0:
    print i, wyjscie[i]
