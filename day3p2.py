import unittest
import operator
from ddt import ddt, data, unpack

def tupleadd(t1, t2):
	return tuple(map(operator.add, t1, t2))

def crunch(number):
	# right, up, left, down
	directions = [(1,0),(0,1),(-1,0),(0,-1)]
	neighbors = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
	# track the tour.  2x1, 2x2, 2x3...
	tier = 1
	stepsontier = 1
	timesontier = 0
	stepnum = 0
	direction = 0
	# track the coordinate and sum, and set initial value
	coord = (0,0)		
	value = 1
	# track spiral on a grid
	spiral = {coord:value}

	while (value < number):

		# walk the spiral
		coord = tupleadd(coord, directions[direction])
		stepnum += 1

		# set the value
		value = 0
		for n in neighbors:
			ncoord = tupleadd(coord, n)
			if ncoord in spiral:
				value += spiral[ncoord]
		spiral[coord] = value
		print("coord: "+str(coord)+" value: "+str(value))

		# deal with direction changes
		if (stepnum == stepsontier):
			print("changing direction")
			#if tier odd, increase steps on tier by 1
			timesontier +=1 
			if (timesontier == 2):
				stepsontier += 1
				timesontier = 0
			#reset steps and change direction
			stepnum = 0
			direction = (direction+1)%4

	return value



@ddt
class testcrunch(unittest.TestCase):

	@data((800, 806), (50, 54), (329, 330))
	@unpack
	def test_cruncher(self, input, result):
		self.assertEqual(crunch(input), result)
		
if __name__ == '__main__':
	#unittest.main()
	print crunch(347991)