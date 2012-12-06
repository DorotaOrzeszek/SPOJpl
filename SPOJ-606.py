import string

t = input()						# liczba testow
for i in range (0,t):
	data = raw_input()
	tab = string.split(data)
	for i in range (1,len(tab)):
		print tab[-i],
	print 
