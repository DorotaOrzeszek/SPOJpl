import copy
t = int(raw_input())
pow16 = [65536, 4096, 256, 16, 1]
pow11 = [161051, 14641, 1331, 121, 11, 1]
ch16 = "0123456789ABCDEF"
ch11 = "0123456789A"
while t > 0:
  a = int(raw_input())
  b = copy.copy(a)
  ans16 = ""
  ans11 = ""
  for i in range(0,len(pow16)):
    curpow16 = pow16[i]
    curpow11 = pow11[i]
    if (a >= curpow16) or (a < curpow16 and len(ans16) > 0):
  		indexa = a/curpow16
  		ans16 += ch16[indexa]
  		a -= indexa * curpow16
		if (b >= curpow11) or (b < curpow11 and len(ans11) > 0):
		  indexb = b/curpow11
		  ans11 += ch11[indexb]
		  b -= indexb * curpow11
  ans11 += ch11[b]
  print ans16, ans11
  t -= 1
