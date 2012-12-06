while True:
  try:
    wejscie = raw_input()
  except EOFError:
    break
  wyjscie = ''
  isTag = False  
  for char in wejscie:
    if char == '<':
      isTag = True
    if char == '>':
      isTag = False
    if isTag == False:
      wyjscie += char
    if isTag == True:
      wyjscie += char.upper()
  print wyjscie
