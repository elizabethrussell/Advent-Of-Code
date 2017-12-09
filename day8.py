import unittest
import operator

def crunch(file):
	ops = {"inc": operator.add, "dec": operator.sub, ">": operator.gt, "<": operator.lt, ">=": operator.ge, "<=":operator.le, "==":operator.eq, "!=":operator.ne}
	registers = {}
	maxval = 0

	lines = file.split('\n')
	for line in lines:
		sides = line.split('if')
		left = sides[0].split()
		right = sides[1].split()

		# check right side condition
		if right[0] not in registers:
			registers[right[0]] = 0
		shouldmodify = ops[right[1]](registers[right[0]],int(right[2]))

		# left side modify
		if shouldmodify:
			if left[0] not in registers:
				registers[left[0]] = 0
			registers[left[0]] = ops[left[1]](registers[left[0]],int(left[2]))
			if registers[left[0]]>maxval:
				maxval = registers[left[0]]

	return maxval



if __name__ == '__main__':
	input = open('day8input').read()
	print crunch(input)
