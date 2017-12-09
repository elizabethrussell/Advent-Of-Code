import unittest


def crunch(input):
	lines = input.split("\n")
	highestdisc = lines[0].split()[0]
	del lines[0]
	keepgoing = True
	changes = 1

	#n^2
	while changes > 0:
		changes = 0
		for line in lines:
			disc = line.split()[0]
			if "->" in line:
				children = [child.strip(' ') for child in (line.split("->")[1].split(','))]
				if highestdisc in children:
					lines.remove(line)
					highestdisc = disc
					changes += 1

		

	return highestdisc
	

class testcrunch(unittest.TestCase):

	def test_cruncher(self):
		self.assertEqual(crunch(testinput), 4)
		

if __name__ == '__main__':
	#unittest.main()
	input = open('day7input').read()
	print crunch(input)
