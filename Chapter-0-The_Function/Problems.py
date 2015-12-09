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
	tuple_sum = []
	for index in range(len(A)):
		tuple_sum.append((A[index][0] + B[index][0], A[index][1] + B[index][1]))
	return tuple_sum
# >>> Problems.tuple_sum([(1,2),(10,20)],[(3,4),(30,40)])
# [(4, 6), (40, 60)]

# Problem 0.8.4 inv_dict(d)
# input: dictionary d representing an invertible function f
# output: dictionary representing the inverse of f, the returned dictionary's keys are the values
# of d and its values are the keys of d
# Example: given an English-French dictionary
# {'thank you': 'merci', 'goodbye', 'au revoir'}
# return a French-English dictionary
# {'merci':'thank you', 'au revoir': 'goodbye'}
def inv_dict(d):
	return {y:x for x,y in d.items()}
# >>> Problems.inv_dict({'thank you': 'merci', 'goodbye': 'au revoir'})
# {'au revoir': 'goodbye', 'merci': 'thank you'}

# Problem 0.8.5
# First write a procedure row(p, n) with the following spec:
# input: integer p, integer n
# output: n-element list such that element i is p+i
# example: given p = 10 and n = 4, return [10,11,12,13]
# Next write a comprehension whose value is a 15-element list of 20-element lists such that the jth element of the ith list is i + j
# You can use row(p, n) in your comprehension.
# Finally, write the same comprehension but without using row(p, n). Hint: replace the call to row(p, n) with the comprehension
# that forms the body of row(p, n)
def row(p, n):
	return list(range(p,p+n))
# >>> Problems.row(10,4)
# [10, 11, 12, 13]
def comprehensionWithRow():
	p = 1 # Arbitrary; could be anything
	return [row(x, 20) for x in row(p, 15)]
# >>> Problems.comprehensionWithRow()
#[
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 
#[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 
#[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 
#[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], 
#[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
#[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 
#[7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], 
#[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], 
#[9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], 
#[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], 
#[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 
#[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], 
#[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], 
#[14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], 
#[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
#]
# (Personally formatted so easier to look at)
def comprehensionWithoutRow():
	return [list(range(x, x+20)) for x in list(range(1, 1+15))]
# >>> Problems.comprehensionWithoutRow()
#[
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 
#[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 
#[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 
#[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], 
#[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
#[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 
#[7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26], 
#[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], 
#[9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], 
#[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], 
#[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 
#[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], 
#[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], 
#[14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33], 
#[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
#]
# (Personally formatted so easier to look at)
