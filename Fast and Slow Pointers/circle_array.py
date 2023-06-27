class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        def shift_index(nums, i):
            n = len(nums)
            return (n + nums[i] + i) % n

        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = shift_index(nums, i)
            direction = True if nums[i] > 0 else False  # direction of the loop

            while (nums[fast] > 0) == direction and (nums[shift_index(nums, fast)] > 0) == direction:
                if slow == fast:
                    if slow == shift_index(nums, slow):  # single length
                        break
                    return True

                slow = shift_index(nums, slow)
                fast = shift_index(nums, shift_index(nums, fast))

        return False