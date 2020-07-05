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


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))