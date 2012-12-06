while True:
	try:
		wejscie = raw_input()
		print wejscie[::-1]
	except EOFError:
		break
