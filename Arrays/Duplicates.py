# Leetcode 217: Given an array of integers, find if the array
# contains any duplicates.

def containsDuplicate(nums: List[int]) => bool:
  seen = set()
  for num in nums:
    if num in seen:
      return True
    else:
  seen.add(num)
return False
