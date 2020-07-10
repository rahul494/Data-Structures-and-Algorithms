# Leetcode 443. String Compression

# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.

# Input:
# ["a","a","b","b","c","c","c"]

# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        index = 0
        i = 0

        # iterate through entire input array
        while (i < len(chars)):
            j = i

            # iterate through repreated characters
            while(j < len(chars) and chars[j] == chars[i]):
                j += 1

            chars[index] = chars[i]
            index += 1

            # append compression length only if length is greater than 1
            # e.g. 'bbbb' is compressed to 'b4', but 'b' remains as 'b'
            if(j - i > 1):
                for c in list(str(j - i)):
                    chars[index] = c
                    index += 1

            # set pointer to new character position
            i = j

        return index


sol = Solution()
assert sol.compress([]) == 0
assert sol.compress(['a']) == 1  #a
assert sol.compress(['a', 'b', 'b', 'b']) == 3  #ab3
assert sol.compress(['a', 'a', 'b', 'b', 'b']) == 4  #a2b3
assert sol.compress(['a', 'b', 'b', 'b', 'c' , 'c', 'c']) == 5  #ab3c3
assert sol.compress(['a', 'a', 'a', 'b', 'b', 'b', 'c' , 'c', 'c']) == 6  #a3b3c3
assert sol.compress(['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']) == 4  #ab12
assert sol.compress(['a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']) == 5  #a2b12

print("All tests have passed sucessfully")
