import unittest
<<<<<<< HEAD
from ddt import ddt, data, unpack


def crunch(number):

	spiral = {}
	writenumber = 1
	travel = 1
	newtravel = false

	while (writenumber < number):
		



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
=======
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

>>>>>>> origin/master


@ddt
class testcrunch(unittest.TestCase):

<<<<<<< HEAD
	@data((4,4), (5,5), (23, 806))
=======
	@data((800, 806), (50, 54), (329, 330))
>>>>>>> origin/master
	@unpack
	def test_cruncher(self, input, result):
		self.assertEqual(crunch(input), result)
		
if __name__ == '__main__':
	#unittest.main()
	print crunch(347991)