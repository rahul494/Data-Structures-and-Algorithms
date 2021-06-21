# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

def isAnagram(s, t):

    hist = {}

    for letter in s:
        if letter in hist:
            hist[letter] += 1
        else:
            hist[letter] = 1

    for letter in t:
        if letter in hist:
            if hist[letter] == 1:
                del hist[letter]
            else:
                hist[letter] -= 1
        else:
            return False

    return True if hist == {} else False


print(isAnagram("nagaram", "anagram"))
print(isAnagram("rat", "cat"))
print(isAnagram("a", "ab"))
