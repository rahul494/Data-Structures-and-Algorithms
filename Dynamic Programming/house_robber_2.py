def rob(nums) -> int:
    if len(nums) <= 3:
        return max(nums)

    nums[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        nums[i] = max(nums[i - 1], nums[i-2] + nums[i])

    if nums[-2] != nums[-1] - nums[0]:
        return max(nums[-2], nums[-1] - nums[0])
    else:
        return nums[-1] - nums[-3]

print(rob([1,2,1,1]))