# 1464. Maximum Product of Two Elements in an Array

# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

# Example 1:

# Input: nums = [3,4,5,2]
# Output: 12
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    max1 = max(nums[0], nums[1])
    max2 = min(nums[0], nums[1])

    for i in range(2, len(nums)):
        if max1 < nums[i] and max2 < nums[i]:
            temp = max1
            max1 = nums[i]
            max2 = temp
        elif max2 < nums[i]:
            max2 = nums[i]

    return (max1-1)*(max2-1)

assert maxProduct([1, 2]) == 0
assert maxProduct([-1, 2]) == -2
assert maxProduct([3, 2, 5]) == 8
assert maxProduct([3, 4, 5, 2]) == 12
assert maxProduct([3, -1, 4, 5, 2]) == 12

print('All tests have passed sucessfully')