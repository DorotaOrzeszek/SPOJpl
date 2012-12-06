import string
while 1:
	try:
		line = raw_input()
	except EOFError:
		break
	list = string.split(line)
	k = list[0]
	n = list[1]
	n = int(n)
	sum = 0
	for i in range(2,n+2):
		if list[i] == k:
			sum = sum+1
	print sum
