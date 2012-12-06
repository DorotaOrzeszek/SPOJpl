t = input()
for i in range (0,t):
	P = raw_input()
	p = str(P)
	one = int(p[0])
	two = int(p[1])
	three = int(p[2])
	four = int(p[3])
	five = int(p[4])
	six = int(p[5])
	seven = int(p[6])
	eight = int(p[7])
	nine = int(p[8])
	ten = int(p[9])
	eleven = int(p[10])
	sum = one+3*two+7*three+9*four+five+3*six+7*seven+9*eight+nine+3*ten+eleven
	if sum % 10 == 0:
		print 'D'
	else:
		print 'N'
