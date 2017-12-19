

def knothash( inputascii):
	listsize = 256
	curpos = 0
	skipsize = 0
	mylist = []
	# build list
	for i in range(0, listsize):
		mylist.append(i)

	# build inputs
	inputs = []
	for char in inputascii:
		inputs.append(ord(char))
	for member in [17,31,73,47,23]:
		inputs.append(member)

	# go
	for x in range(0,64): #run 64 times
		for input in inputs:
			sublist = []
			for i in range(curpos, curpos+input):
				sublist.append(mylist[i%listsize])
			sublist.reverse()
			for i in range(curpos, curpos+input):
				index = i % listsize
				mylist[index] = sublist[i-curpos]
			curpos = (curpos + skipsize + input)%listsize
			skipsize += 1

	xors = []
	xi = 0
	for i in range(0, 256, 16):
		xors.append(0)
		for j in range(0, 16):
			xors[xi] = xors[xi] ^ mylist[i+j]
		xi += 1

	finalstr = ""
	for x in xors:
		finalstr += ('{0:02x}'.format(x))

	return finalstr

def crunch(key):
	hexDict = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'a':'1010', 'b':'1011', 'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111'}
	total = 0
	for i in range(0, 128):
		hashinput = key + "-"+str(i)
		output = knothash(hashinput)
		for c in output: # to binary
			binary = hexDict[c]
			zeros = binary.count('1')
			total += zeros
	return total


if __name__ == '__main__':
	testinput = "flqrgnkx"
	realinput = "uugsqrei"
	print crunch(realinput)
