while True:
	try:
		wejscie = raw_input()
	except EOFError:
		break
	if not wejscie:
		break
	c = wejscie.split()[0]
	word = wejscie.split()[1]
	wyjscie = ""
	for x in word:
		if x != c:
			wyjscie += x
	print wyjscie
