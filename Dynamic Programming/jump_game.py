class Solution:
    def canJump(self, nums):
        n = len(nums)
        i = 1
        
        if nums[0] == 0 and n > 1:
            return False

        while i < n:
            nums[i] = max(nums[i], nums[i - 1] - 1)

            if nums[i] == 0 and i < n-1:
                return False
            i += 1

        print(nums)
        return True
    
s = Solution()
print(s.canJump([3,2,1,0,4]))