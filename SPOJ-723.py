import string
t = input()
for i in range (0,t):
	tekst = raw_input()
	tab = string.split(tekst)
	for j in range (2,len(tab)):
		print tab[j],
	print tab[1]
