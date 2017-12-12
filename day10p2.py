import unittest
from ddt import ddt, data, unpack


def crunch( inputascii):
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
			print "i: "+str(i)+" j: "+str(j)
			xors[xi] = xors[xi] ^ mylist[i+j]
		xi += 1

	finalstr = ""
	for x in xors:
		finalstr += ('{0:02x}'.format(x))


	print finalstr

	return finalstr


@ddt
class testcrunch(unittest.TestCase):

	@data(("","a2582a3a0e66e6e86e3812dcb672a272"),("AoC 2017","33efeb34ea91902bb2f59c9920caa6cd"),("1,2,3","3efbe78a8d82f29979031a4aa0b16a9d"))
	@unpack
	def test_cruncher(self, input, result):
		self.assertEqual(crunch(input), result)


if __name__ == '__main__':
	#unittest.main()
	realinput = "83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100"
	print crunch(realinput)
