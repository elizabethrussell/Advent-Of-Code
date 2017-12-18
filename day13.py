

def crunch(input):
	# build puzzle from input
	layers = {}
	lines = input.split('\n')
	toplayer = 0
	for line in lines:
		nums = line.split(': ')
		toplayer = int(nums[0])
		layers[toplayer] = (int(nums[1]),0,True)

	severity = 0
	myposition = -1
	for i in xrange(0, toplayer+1):
		#i move
		myposition += 1

		#increment if caught
		if myposition in layers:
			caught = (layers[myposition][1] == 0)
			if caught:
				severity += (myposition * layers[myposition][0])

		#scanners move
		for layer, state in layers.iteritems():
			newscannerposition = 0
			# at bottom
			if (state[2] and state[1] == state[0]-1):
				layers[layer] = (state[0], state[0]-2, False)
			# at top
			elif (not state[2] and state[1]==0):
				layers[layer] = (state[0], 1, True)
			# moving up
			elif (state[2]):
				layers[layer] = (state[0], state[1]+1, True)
			# moving down
			else:
				layers[layer] = (state[0], state[1]-1, False)



	return severity



if __name__ == '__main__':
	input = open('day13input').read()
	print crunch(input)