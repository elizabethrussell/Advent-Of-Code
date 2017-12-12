import unittest
from ddt import ddt, data, unpack


def crunch(arr):
	opengroups = 0
	score = 0
	garbage = False
	garbagechars = 0
	i = 0
	while i < len(arr):
		if arr[i] == '!':
			i += 1
		elif arr[i] == '<' and not garbage:
			garbage = True 
		elif arr[i] == '>' and garbage:
			garbage = False
		elif arr[i] == '{' and not garbage:
			opengroups += 1
		elif arr[i] == '}' and not garbage:
			score += opengroups 
			opengroups += -1
		elif garbage:
			garbagechars += 1
		i += 1

	return garbagechars
	

@ddt
class testcrunch(unittest.TestCase):

	@data(("{}",1), ("{{{}}}",6), ("{{},{}}",5), ("{{{},{},{{}}}}",16), ("{<a>,<a>,<a>,<a>}",1),("{{<!!>},{<!!>},{<!!>},{<!!>}}",9),("{{<a!>},{<a!>},{<a!>},{<ab>}}",3))
	
	@unpack
	def test_cruncher(self, input, result):
		self.assertEqual(crunch(input), result)
		

if __name__ == '__main__':
	input = open('day9input').read()

	#unittest.main()
	print crunch(input)
