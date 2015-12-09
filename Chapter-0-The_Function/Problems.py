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

# Problem 0.8.3 tuple_sum(A, B)
# input: lists A and B of the same length, where each element in each list is a pair (x,y) of numbers
# output: list of pairs (x,y) in which the first element of the ith pair is the sum of the first element
# of the ith pair in A and the first element of the ith pair in B
# Example: given lists [(1,2),(10,20)] and [(3,4),(30,40)], return [(4,6),(40,60)]
def tuple_sum(A, B):
	return [(xA + xB, yA + yB) for (xA, yA) in A for (xB, yB) in B]
# >>> Problems.tuple_sum([(1,2),(10,20)],[(3,4),(30,40)])
# [(4, 6), (31, 42), (13, 24), (40, 60)]