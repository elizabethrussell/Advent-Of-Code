import unittest
import re

def crunch(input):
	# lines = input.split("\n")
	# highestdisc = lines[0].split()[0]
	# del lines[0]
	# keepgoing = True
	# changes = 1

	# # find highest disc
	# while changes > 0:
	# 	changes = 0
	# 	for line in lines:
	# 		disc = line.split()[0]
	# 		if "->" in line:
	# 			children = [child.strip(' ') for child in (line.split("->")[1].split(','))]
	# 			if highestdisc in children:
	# 				lines.remove(line)
	# 				highestdisc = disc
	# 				changes += 1

	# build an easier struct- dictionaries childmap and weightmap for fast lookup
	lines = input.split("\n")
	childmap = {}
	weightmap = {}
	for line in lines:
		discinfo = line.split()
		disc = discinfo[0]
		weight = int(re.sub('[() ]', '', discinfo[1]))
		weightmap[disc] = weight
		if "->" in line:
			children = [child.strip(' ') for child in (line.split("->")[1].split(','))]
			childmap[disc] = children


	# recursive function for finding load at each point
	def findload(disc):
		if disc not in childmap:
			return 0
		else:
			myload = 0
			for child in childmap[disc]:
				addable = findload(child)
				myload += weightmap[child] + addable
			return myload


	#populate the load on each disc
	loadmap = {}
	for disc in weightmap:
		loadmap[disc] = findload(disc)
		#print disc + ": " + str(findload(disc))		

	#crawl starting with the top node
	bottom = "azqje"
	#bottom = "tknk"

	def investigate(node, ans):
		print "investigating "+ node
		childloads = {}
		if node not in childmap:
			return None
		else:
			for child in childmap[node]:
				loadonbottom = weightmap[child]+loadmap[child]
				if loadonbottom in childloads:
					childloads[loadonbottom].append(child)
				else:
					childloads[loadonbottom] = [child]
			#print childloads
			if len(childloads) > 1: # found imbalance
				for load in childloads:
					cs = childloads[load]
					if len(cs) < 2:
						if(investigate(cs[0], cs[0])) is None:
							print "node is "+cs[0]
							print "node weight is "+str(weightmap[cs[0]])
							difference = (childloads.keys()[0]-childloads.keys()[1])
							print "difference is "+ str(difference)
							print 
							return difference

	a = investigate(bottom, bottom)


	return a
	

class testcrunch(unittest.TestCase):

	def test_cruncher(self):
		self.assertEqual(crunch(testinput), 4)
		

if __name__ == '__main__':
	#unittest.main()
	input = open('day7input').read()
	print crunch(input)
