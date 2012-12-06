import string
table = string.maketrans('abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')
while 1:
	try:
		text = raw_input()
	except EOFError:
		break
#	text = string.capwords(text)
	text2 = string.split(text)
	for i in range (1,len(text2)):
		first = text2[i][0]
		first = string.translate(first,table)
		text2[i] = first+text2[i][1:]
#	print reduce(lambda a,b:a+b, text2)
	sum = ''
	for slowo in text2:
		sum = sum + slowo
	print sum
