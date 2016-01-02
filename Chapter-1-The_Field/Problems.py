# Author: Tim Kwist

# Python comprehension problems
# Write each of the following three procedures using a comprehension:

# Problem 1.7.1: my_filter(L, num)
# Input: list of numbers and a positive integer.
# Output: list of numbers not containing a multiple of num
# Example: given list = [1,2,4,5,7] and num = 2, return [1,5,7]
def my_filter(L, num):
	return [x for x in L if x % num != 0]

# Problem 1.7.2: my_lists(L)
# Input: list L of non-negative integers
# Output: a list of lists: for every element x in L create a list containing 1,2,...x.
# Example: given [1,2,4] return [[1], [1,2],[1,2,3,4]].
# Example: given [0] return [[]]
def my_lists(L):
	return [list(range(1,x+1)) for x in L]

# Problem 1.7.3: my_function_composition(f,g)
# Input: two functions f and g, represented as dictionaries, such that g of f exists
# Output: dictionary that represents the function g of f
# Example: given f = {0:'a', 1:'b'} and g = {'a':apple, 'b':'banana'}, return {0:'apple', 1:'banana'}
def my_function_composition(f,g):
	return {x:g[y] for x, y in f.items()}