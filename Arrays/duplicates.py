# 217. Contains Duplicate

# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:

# Input: [1,2,3,1]
# Output: true
  
# Example 2:

# Input: [1,2,3,4]
# Output: false


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False


assert containsDuplicate([1]) == False
assert containsDuplicate([1, 1]) == True
assert containsDuplicate([1, 1, 1]) == True
assert containsDuplicate([1, 2]) == False
assert containsDuplicate([1, 1, 1, 2, 2]) == True
assert containsDuplicate([-1, 1]) == False
assert containsDuplicate([10, 20, 200, 10, 200, 250, 10]) == True

print('All tests have passed sucessfully')