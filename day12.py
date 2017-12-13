import unittest
from ddt import ddt, data, unpack


def crunch(input):
	lines = input.split('\n')

	friends = {}

	for line in lines:
		sides = line.split('<->')
		key = int(sides[0].strip())
		if key not in friends:
			friends[key] = []
		for val in sides[1].split(','):
			friends[key].append(int(val.strip()))

	# crawl
	gathered = set()
	searched = set()

	def gatherchildren(n):
		# gather
		if n not in gathered:
			gathered.add(n)

		if n in searched:
			#stop search
			return
		else:
			searched.add(n)
			for child in friends[n]:
				gatherchildren(child)



	for child in friends[0]:
		gatherchildren(child)



	return len(gathered)
	


if __name__ == '__main__':
	input = open('day12input').read()

	#unittest.main()
	print crunch(input)
