import string
t = input()
for i in range (0,t):
	tekst = raw_input()
	tab = string.split(tekst)
	a = int(tab[0])
	b = int(tab[1])
	x = min(a,b)
	y = max(a,b)
	r = 1
	while r > 0:
		r = y % x
		y = x
		x = r
	nwd = y
	print nwd
