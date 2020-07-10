# Leetcode - 283. Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    index = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1

    for i in range(index, len(nums)):
        nums[i] = 0

    return nums


assert moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert moveZeroes([0, 1, 0, 0, 0]) == [1, 0, 0, 0, 0]
assert moveZeroes([-1, 1, -5, 3, 12]) == [-1, 1, -5, 3, 12]
assert moveZeroes([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
assert moveZeroes([0, 1, 0]) == [1, 0, 0]
assert moveZeroes([0, 1]) == [1, 0]
assert moveZeroes([0]) == [0]
assert moveZeroes([1]) == [1]

print('All tests have passed sucessfully')
