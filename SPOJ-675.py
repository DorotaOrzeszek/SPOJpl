D = int(raw_input())
while D > 0:
  N = int(raw_input())
  wskazowki = [0,0,0,0] # [N,S,W,E]
  while N > 0:
    wejscie = raw_input()
    wejscie2 = wejscie.split()
    if wejscie2[0] == '0':
      wskazowki[0] += int(wejscie2[1])
    elif wejscie2[0] == '1':
      wskazowki[1] += int(wejscie2[1])
    elif wejscie2[0] == '2':
      wskazowki[2] += int(wejscie2[1])
    elif wejscie2[0] == '3':
      wskazowki[3] += int(wejscie2[1])
    N -= 1
  krokiNS = max(wskazowki[0]-wskazowki[1], wskazowki[1]-wskazowki[0])
  if wskazowki[0] >= wskazowki[1]:
    kierunekNS = '0'
  else:
    kierunekNS = '1'
  krokiWE = max(wskazowki[2]-wskazowki[3], wskazowki[3]-wskazowki[2])
  if wskazowki[2] >= wskazowki[3]:
    kierunekWE = '2'
  else:
    kierunekWE = '3'  

  if krokiNS == 0 and krokiWE == 0:
    print 'studnia'
  elif krokiNS == 0 and krokiWE != 0:
    print kierunekWE + ' ' + str(krokiWE)
  elif krokiNS != 0 and krokiWE == 0:
    print kierunekNS + ' ' + str(krokiNS)
  else:
    print kierunekNS + ' ' + str(krokiNS)
    print kierunekWE + ' ' + str(krokiWE)
  D -= 1
