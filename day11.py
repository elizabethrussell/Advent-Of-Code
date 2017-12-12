import unittest
from ddt import ddt, data, unpack


def crunch(arr):
	x = 0
	y = 0
	z = 0
	maxdistance = 0
	for dir in arr.split(','):
		if dir == 'n':
			x += 1
			z += -1
		elif dir == 'ne':
			x += 1
			y += -1
		elif dir == 'se':
			y += -1
			z += 1
		elif dir == 's':
			x += -1
			z += 1
		elif dir == 'sw':
			x += -1
			y += 1
		elif dir == 'nw':
			y += 1
			z += -1
		dist = (abs(x) + abs(y) + abs(z))/2
		if dist>maxdistance:
			maxdistance = dist

	return maxdistance
	

@ddt
class testcrunch(unittest.TestCase):

	@data(("ne,ne,ne",3), ("ne,ne,sw,sw",0), ("ne,ne,s,s",2), ("se,sw,se,sw,sw",3))
	
	@unpack
	def test_cruncher(self, input, result):
		self.assertEqual(crunch(input), result)
		

if __name__ == '__main__':
	input = open('day11input').read()

	#unittest.main()
	print crunch(input)
