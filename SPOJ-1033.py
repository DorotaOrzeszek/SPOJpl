t = [0,0]
while not (t[0] == 42 and t[1] == 42):
	x = input()
	print x
	t[1] = t[0]
	t[0] = x
