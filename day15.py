
def crunch(startA, startB):
	a = startA
	b = startB
	count = 0
	for i in range(0, 40000000):
		a = (a*16807)%2147483647
		b = (b*48271)%2147483647
		if ((a&0xffff)^(b&0xffff)==0):
			count += 1
	return count


if __name__ == '__main__':
	print crunch(679, 771)