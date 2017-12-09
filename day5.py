import unittest
import urllib2
from ddt import ddt, data, unpack


def crunch(str):
	array = map(int, str.split())
	numsteps = 0
	i = 0
	while(0 <= i < len(array)):
		icpy = i
		i += array[i]
		if (array[icpy] >= 3):
			array[icpy] += -1
		else:
			array[icpy] += 1
		numsteps += 1
	return numsteps
	

puzzleinput = "0\n3\n0\n1\n-3"
class testcrunch(unittest.TestCase):

	def test_cruncher(self):
		self.assertEqual(crunch(puzzleinput), 10)
		

if __name__ == '__main__':
	#unittest.main()
	input = open('day5input').read()
	print crunch(input)
