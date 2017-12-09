import unittest


def crunch(input):
	banks = map(int, input.split())
	strbanks = ''.join(str(e) for e in banks)
	numsteps = 0
	seenset = set()
	totalblocks = len(banks)

	while(strbanks not in seenset):
		seenset.add(strbanks)
		renumber = max(banks)
		reindex = banks.index(renumber)
		banks[reindex] = 0
		for i in range(0, renumber):
			index = (reindex + 1 + i)%totalblocks
			banks[index] += 1
		strbanks = ''.join(str(e) for e in banks)

	#now run until we see strbanks again
	strnext = ""
	while (strnext != strbanks):
		numsteps += 1
		renumber = max(banks)
		reindex = banks.index(renumber)
		banks[reindex] = 0
		for i in range(0, renumber):
			index = (reindex + 1 + i)%totalblocks
			banks[index] += 1
		strnext = ''.join(str(e) for e in banks)



	return numsteps
	
testinput = "0 2 7 0"
finalinput = "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"

class testcrunch(unittest.TestCase):

	def test_cruncher(self):
		self.assertEqual(crunch(testinput), 4)
		

if __name__ == '__main__':
	#unittest.main()
	#input = open('day5input').read()
	print crunch(finalinput)
