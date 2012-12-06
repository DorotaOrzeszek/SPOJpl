import string
t = input()
for i in range (0,t):
	slowa = raw_input()
	tab = string.split(slowa)
	max = min(len(tab[0]),len(tab[1]))
	odp = ''
	for j in range(0,max):
		odp = odp+tab[0][j]
		odp = odp+tab[1][j]
	print odp
