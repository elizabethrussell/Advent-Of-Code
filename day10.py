

def crunch(listsize, inputs):
	curpos = 0
	skipsize = 0
	mylist = []
	for i in range(0, listsize):
		mylist.append(i)

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


	return mylist[0]*mylist[1]



if __name__ == '__main__':
	testlength = 5
	testinput = [3,4,1,5] # 12
	length = 256
	realinput = [83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100]
	print crunch(length, realinput)
