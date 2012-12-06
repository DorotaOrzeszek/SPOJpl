slowa = {1:'jeden',2:'dwa',3:'trzy',
4:'cztery',5:'piec',6:'szesc',7:'siedem',
8:'osiem',9:'dziewiec',10:'dziesiec',
11:'jedenascie',12:'dwanascie',13:'trzynascie',
14:'czternascie',15:'pietnascie',16:'szesnascie',
17:'siedemnascie',18:'osiemnascie',19:'dziewietnascie',
20:'dwadziescia',30:'trzydziesci',40:'czterdziesci',
50:'piecdziesiat',60:'szescdziesiat',70:'siedemdziesiat',
80:'osiemdziesiat',90:'dziewiecdziesiat',
100:'sto',200:'dwiescie',300:'trzysta',
400:'czterysta',500:'piecset',600:'szescset',
700:'siedemset',800:'osiemset',900:'dziewiecset',
1000:'tys.',1000000:'mln.',1000000000:'mld.',
1000000000000:'bln.'}

def czytTys(n):
  # n = xyz string
  # x00  yz  y0  z
  czytliczbe = []
  if int(n) >= 100:
    czytliczbe.append(slowa[int(n[0]+'00')])
  if int(n[1:]) <= 20:
    if int(n[1:]) == 0:
      pass
    else:
      czytliczbe.append(slowa[int(n[1:])])
  if int(n[1:]) > 20:
    czytliczbe.append(slowa[int(n[1]+'0')])
    if int(n[2]) != 0:
      czytliczbe.append(slowa[int(n[2])])
  return czytliczbe

t = input()
while t > 0:
  wejscie = raw_input()
  dlugosc = len(wejscie)
  liczba = wejscie.zfill(13)
  odp = []
  
  if liczba[0] == '1':
    odp.append(slowa[1])
    odp.append(slowa[1000000000000])
  if liczba[1:4] != '000':
    odp.append(czytTys(liczba[1:4]))
    odp.append(slowa[1000000000])
  if liczba[4:7] != '000':
    odp.append(czytTys(liczba[4:7]))
    odp.append(slowa[1000000])
  if liczba[7:10] != '000':
    odp.append(czytTys(liczba[7:10]))
    odp.append(slowa[1000])
  if liczba[10:13] != '000':
    odp.append(czytTys(liczba[10:13]))
  for element in odp:
    if type(element) is str:
      print element,
    else:
      for el in element:
        print el, 
  t -= 1
