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
	searched = set()

	def gatherchildren(n, seed):
		if n == seed:
			return
		# gather
		if n not in friends[seed]:
			friends[seed].append(n)

		if n in searched:
			#stop search
			return
		else:
			searched.add(n)
			for child in friends[n]:
				gatherchildren(child, seed)
			del friends[n]


	groups = 0
	while len(friends) > 0:
		index = friends.keys()[0]
		for child in friends[index]:
			gatherchildren(child, index)
		groups += 1
		del friends[index]


	#set size = len(friends[x])+1 where 1 is from the identity relationship

	return groups
	


if __name__ == '__main__':
	input = open('day12input').read()

	#unittest.main()
	print crunch(input)
