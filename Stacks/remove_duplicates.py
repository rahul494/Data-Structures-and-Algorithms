class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            
            if len(stack) == 0:
                stack.append(s[i])
            elif s[i] == stack[len(stack) - 1]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return ''.join(stack)
        

s = Solution()
print(s.removeDuplicates("abbaca"))