t = input()
while t > 0:
	wejscie = raw_input()
	x = int(wejscie.split()[0])
	n = int(wejscie.split()[1])
	p = int(wejscie.split()[2])
	wyjscie = x**n%p
	print wyjscie
	t -= 1
