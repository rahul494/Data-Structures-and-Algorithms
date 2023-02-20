class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        index = 2
        
        while index < len(cost):
            cost[index] = min(cost[index-1] + cost[index], cost[index - 2] + cost[index])
            index += 1

        return min(cost[len(cost) -1], cost[len(cost) - 2])      
            

s = Solution()
print(s.minCostClimbingStairs([10,15,20]))
        

