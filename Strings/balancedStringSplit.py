# 1221. Split a String in Balanced Strings

# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.

# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Example 2:

# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        r_count = 0
        l_count = 0
        for ele in s:
            if ele == 'R':
                r_count += 1
                if r_count ==  l_count:
                    result += 1
                    r_count = 0
                    l_count = 0
            else:
                l_count += 1
                if r_count ==  l_count:
                    result += 1
                    r_count = 0
                    l_count = 0
        
        return result
