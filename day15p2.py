
def crunch(startA, startB):
	a = startA
	b = startB
	count = 0
	for i in range(0, 5000000):
		startovera = True
		startoverb = True
		while (startovera or a%4>0): 
			a = (a*16807)%2147483647
			startovera = False
		while (startoverb or b%8>0):
			b = (b*48271)%2147483647
			startoverb = False
		if ((a&0xffff)^(b&0xffff)==0):
			count += 1
	return count


if __name__ == '__main__':
#print crunch(65, 8921)
	print crunch(679, 771)