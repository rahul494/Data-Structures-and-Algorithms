import math

class Solution:
    def average(self, salary):
        total, min_sal, max_sal = 0, math.inf, -math.inf

        for s in salary:
            if min_sal > s:
                min_sal = s
            if max_sal < s:
                max_sal = s
            
            total += s

        return (total - min_sal - max_sal) / (len(salary) - 2)
    
s = Solution()
s.average([4000,3000,1000,2000])