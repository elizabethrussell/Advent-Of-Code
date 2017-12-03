import unittest
from ddt import ddt, data, unpack


def crunch(number):
	#what layer of spiral
	sidelength = 1
	while ((sidelength**2) < number):
		sidelength += 2
	layer = (sidelength - 1) / 2

	# how far  from corner 
	zero1 = (sidelength-2)**2 + (sidelength-1)/2
	zero2 = zero1 + (sidelength-1)
	zero3 = zero2 + (sidelength-1)
	zero4 = zero3 + (sidelength-1)
	# min absolute distance from a zero is the traversal length
	sidedistance = min(abs(number - zero1), abs(number-zero2), abs(number-zero3), abs(number-zero4))

	return layer + sidedistance


@ddt
class testcrunch(unittest.TestCase):

	@data((12,3), (23,2), (1024, 31))
	@unpack
	def test_cruncher(self, input, result):
		self.assertEqual(crunch(input), result)
		
if __name__ == '__main__':
	#unittest.main()
	print crunch(347991)