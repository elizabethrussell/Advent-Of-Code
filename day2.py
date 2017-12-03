import unittest
import urllib2

def crunch(spreadsheet):
	lines = spreadsheet.split('\n')
	checksum = 0
	for line in lines:
		numerals = line.split()
		minn = int(numerals[0])
		maxn = int(numerals[0])
		del numerals[0]
		for nstring in numerals:
			n = int(nstring)
			if n<minn:
				minn = n
			if n> maxn:
				maxn = n
		checksum += maxn - minn
	return checksum	


testspreadsheet = "5 1 9 5\n7 5 3\n2 4 6 8"
testresult = 18

class testcrunch(unittest.TestCase):

	def test_cruncher(self):
		self.assertEqual(crunch(testspreadsheet), testresult)
		

if __name__ == '__main__':
	#unittest.main()
	puzzleinput = open('day2input').read()
	print crunch(puzzleinput)