import unittest
from ddt import ddt, data, unpack

def crunch(spreadsheet):
	lines = spreadsheet.split('\n')
	checksum = 0
	for line in lines:
		if checkphrase(line):
			checksum += 1
	return checksum	

def checkphrase(line):
	wordset = set()
	words = line.split()
	for word in words:
		if word in wordset:
			return False
		wordset.add(word)
	return True


@ddt
class testcrunch(unittest.TestCase):

	@data(('aa bb cc dd ee',True), ('aa bb cc dd aa',False), ('aa bb cc dd aaa',True))
	@unpack
	def test_cruncher(self, line, result):
		self.assertEqual(checkphrase(line), result)
		

if __name__ == '__main__':
	#unittest.main()
	puzzleinput = open('day4input').read()
	print crunch(puzzleinput)