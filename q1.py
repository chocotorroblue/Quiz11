import math
def readNumbersFromFile(x):
	y = open(x, "r")
	total = 0
	l = []
	z = 0
	f = 0
	p = 0
	for line in y:
		total = total + (int(line))
		l.append(int(line))
		value = len(l)
		average = total / value
		while (z < value):
			f = ((l[z]) - average) ** 2
			z = z + 1
			p = p + f
			standard_desviation = math.sqrt(c / value)
	print("Number of values:", value)
	print("Total of values:", total)
	print("Average:", average)
	print("Standard Desviation:", standard_desviation)

readNumbersFromFile("random.txt")
