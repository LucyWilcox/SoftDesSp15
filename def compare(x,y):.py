def compare(x,y):
	if x > y:
		return 1
	elif x < y:
		return -1
	else:
		return 0

#value = compare(2,3)
#print value

def grid(row, column):
	line = ('+ ' + '- '*4) * column +'+'
	notline = ("|         "*(column + 1) + '\n')* 4
	print (line + '\n' + notline)* 4 + line

#grid(4, 4)

def check_fermat(a, b, c, n):
	if c**n == a**n  + b**n:
		print "Holy smokes, Fermat was wrong!"
	else:
		print "No, that doesn't work."

def please_check_fermat():
	a = int(raw_input("choose an a \n"))
	b = int(raw_input("choose a b! \n"))
	c = int(raw_input("choose a c! \n"))
	n = int(raw_input("choose a n! \n"))

	check_fermat(a, b, c, n)

please_check_fermat()

