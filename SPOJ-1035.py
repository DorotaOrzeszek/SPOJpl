wejscie = [0,0,42]
count42 = 0
while True:
	try:
		wejscie.append(input())
	except EOFError:
		break
	if wejscie[-1] == 42 and wejscie[-2] != 42:
		count42 += 1
	print wejscie[-1]
	if count42 == 3:
		break
