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
	sortedwordset = set()
	words = line.split()
	for word in words:
		# check for duplicate word
		if word in wordset:
			return False
		wordset.add(word)
		# check for anagram
		sortedword = sortword(word)
		if sortedword in sortedwordset:
			return False
		sortedwordset.add(sortedword)
	return True

def sortword(word):
	return (''.join(sorted(word)))


@ddt
class testcrunch(unittest.TestCase):

	@data(('abcde fghij',True), ('abcde xyz ecdab',False), ('iiii oiii ooii oooi oooo',True))
	@unpack
	def test_cruncher(self, line, result):
		self.assertEqual(checkphrase(line), result)
		

if __name__ == '__main__':
	#unittest.main()
	puzzleinput = open('day4input').read()
	print crunch(puzzleinput)