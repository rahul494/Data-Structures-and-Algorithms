# AlgoExpert - Validate Subsequence

# Given two non-empty arrays of integers, write a function that determines 
# whether the second array is a subsequence of the first one.

# A subsequence of an array is a set of numbers that aren't necessarily adjacent
# in the array but that are in the same order as they appear in the array. For
# instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4].
# Note that a single number in an array and the array itself are both valid
# subsequences of the array.

# Sample Input
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]

# Output
# true

def isValidSubsequence(array, sequence):
	arr_idx = 0
	seq_idx = 0

	while arr_idx < len(array) and seq_idx < len(sequence):
		if array[arr_idx] == sequence[seq_idx]:
			arr_idx += 1
			seq_idx += 1
		else: 
			arr_idx += 1
			
	return seq_idx == len(sequence)

assert isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]) == True
assert isValidSubsequence([1, 2, 3, 4], [1, 3, 4]) == True
assert isValidSubsequence([1, 2, 3], [1, 2, 3]) == True
assert isValidSubsequence([1, 2, 3], [2, 5]) == False
assert isValidSubsequence([1], [2]) == False

print('All tests have passed sucessfully')
