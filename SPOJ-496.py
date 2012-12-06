D = input()
tab = [[0,1],[0,2],[0,6],[2,4],[2,0],[2,0],[4,0],[2,0],[8,0]]
for i in range (0,D):
	n = input()
	if n >= 10:
		a = 0
		b = 0
		print a, b
	elif n < 1:
		a = 0
		b = 1
		print a, b
	else:
		a = tab[n-1][0]
		b = tab[n-1][1]
		print a, b
