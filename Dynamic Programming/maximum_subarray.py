# Leetcode - 53. Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    resu = nums[0]
    curr_max = nums[0]

    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max + nums[i])

        if resu < curr_max:
            resu = curr_max

    return resu


assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert maxSubArray([1, -7, 4, -1, 21, 1, -5, 9]) == 29
assert maxSubArray([-2, -1, 1]) == 1
assert maxSubArray([-2, 2]) == 2
assert maxSubArray([1]) == 1

print('All tests have passed successfully')
