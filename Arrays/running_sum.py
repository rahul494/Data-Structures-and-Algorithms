# 1480. Running Sum of 1d Array

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums
        else:
            running_sum = [nums[0]]
            for i in range(1, len(nums)):
                running_sum.append(running_sum[i-1] + nums[i])
            return running_sum
