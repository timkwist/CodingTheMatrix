# Author: Tim Kwist

# Python comprehension problems
# Write each of the following three procedures using a comprehension:

# Problem 1.7.1: my_filter(L, num)
# Input: list of numbers and a positive integer.
# Output: list of numbers not containing a multiple of num
# Example: given list = [1,2,4,5,7] and num = 2, return [1,5,7]
def my_filter(L, num):
	return [x for x in L if x % num != 0]