class Solution:
    def is_anagram(self, window, p):
        shallow_window = window.copy()

        for letter in p:
            if letter not in shallow_window:
                return False
            elif shallow_window[letter] < 1:
                return False
            else:
                shallow_window[letter] -= 1
       
        return True
    # s=cbaebabacd
    # p=abc

    def findAnagrams(self, s, p):
        result = []
        window = {}

        for i in range(len(s)):
            # build initial window
            if i < len(p):
                if p[i] in window:
                    window[p[i]] += 1
                else:
                    window[p[i]] = 1

            # check 
            if self.is_anagram(window, s[i - len(p) + 1:i]):
                result.append(i-len(p)+1)
            
            # remove last element
            if i >= len(p) - 1:
                
                if s[i - len(p) + 1] in window:
                    if window[s[i - len(p) + 1]] == 0:
                        del window[s[i - len(p) + 1]]
                    else:
                        window[s[i - len(p) + 1]] -= 1

            print(i)
            print(window)

        return result

s = Solution()
print(s.findAnagrams('cbaebabacd','abc'))
    
