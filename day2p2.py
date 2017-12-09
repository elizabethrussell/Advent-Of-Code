import unittest
import urllib2

def crunch(spreadsheet):
	lines = spreadsheet.split('\n')
	checksum = 0
	for line in lines:
		snumerals = line.split()
		numerals = map(int, snumerals)
		for i in range(0, len(numerals)-1):
			for j in range(i+1, len(numerals)):
				if (numerals[i]%numerals[j] == 0):
					checksum += (numerals[i] / numerals[j])
				if (numerals[j]%numerals[i] == 0):
					checksum += (numerals[j] / numerals[i])
	return checksum



testspreadsheet = "5 9 2 8\n 9 4 7 3\n 3 8 6 5"
testresult = 9

class testcrunch(unittest.TestCase):

	def test_cruncher(self):
		self.assertEqual(crunch(testspreadsheet), testresult)
		

if __name__ == '__main__':
	#unittest.main()
	puzzleinput = open('day2input').read()
	print crunch(puzzleinput)