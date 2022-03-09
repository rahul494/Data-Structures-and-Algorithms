# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    hist = {}

    for i in range(len(nums)):
        if target - nums[i] in hist:
            return [i, hist[target - nums[i]]]
        else:
            hist[nums[i]] = i


def all_pairs(nums, target):

    result = []
    history = {}

    for i in range(len(nums)):

        if target - nums[i] in history:
            result.append(sorted((i, history[target - nums[i]])))
        else:
            history[nums[i]] = i

    return result


print(twoSum([1, 2, 4, 5, 2, 1], 7))
