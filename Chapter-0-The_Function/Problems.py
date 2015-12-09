# Author: Tim Kwist

# Problem 0.8.1
# increments(L)
# input: list L of numbers
# output: line of numbers in which the ith element is one plus the ith element of L
# Example: increments([1,5,7]) should return [2,6,8]
def increments(L):
	return [num + 1 for num in L]
# >>> Problems.increments([1,5,7])
# [2, 6, 8]

# Problem 0.8.2
# cubes(L)
# input: list L of numbers
# output: list of numbers in which the ith element is the cube of the ith element of L
# Example: given [1,2,3] return [1,8,27]
def cubes(L):
	return [num*num*num for num in L]
# >>> Problems.cubes([1,2,3])
# [1, 8, 27]