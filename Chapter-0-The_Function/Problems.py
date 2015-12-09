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
