def lengthOfLongestSubstring(s):
    history = set()
    l = 0
    max_len = 0

    for r in range(len(s)):
        while s[r] in history:
            history.remove(s[l])
            l += 1
        history.add(s[r])
        if len(history) > max_len:
            max_len = len(history)

    return max_len
    
print(lengthOfLongestSubstring('abcabcbb'))