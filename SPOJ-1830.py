import string
while 1:
	try:
		line = raw_input()
	except EOFError:
		break
	values = string.split(line)
	a = values[0]
	a = float(a)
	b = values[1]
	b = float(b)
	c = values[2]
	c = float(c)
	if a>0 and b>0 and c>0 and (a+b > c) and (a+c > b) and (b+c > a):
		print 1
	else:
		print 0
