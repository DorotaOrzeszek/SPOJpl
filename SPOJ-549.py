import string
t = input()
for i in range (0,t):
	n = input()
	liczby = raw_input()
	tab = string.split(liczby)
	suma = 0
	for j in range (0,n):
		suma = suma+int(tab[j])
	print suma
