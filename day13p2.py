

def crunch(input):
	# build puzzle from input
	layers = {}
	lines = input.split('\n')
	toplayer = 0
	for line in lines:
		nums = line.split(': ')
		toplayer = int(nums[0])
		layers[toplayer] = (int(nums[1]),0,True)

	#>194600

	startposition = -190000

	caught = False
	finished = False 
	while (not finished):
		#move back
		startposition += -1
		myposition = -1
		broken = False
		for i in xrange(0, toplayer+1):
			j = i - startposition

			#i move
			myposition += 1

			#increment if caught
			if myposition in layers:
				r = layers[myposition][0]
				pos = j % (r+r-2)
				if (pos == 0):
					broken = True
					break
	
		if not broken:
			break
	wait = 0-startposition

	return wait



if __name__ == '__main__':
	input = open('day13input').read()
	print crunch(input)