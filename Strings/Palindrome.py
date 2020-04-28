# AlgoExpert - Palindrome Check

# A palindrome is defined as a string that's written the same forward and
# backward. Note that single-character strings are palindromes.

# Write a function that takes in a non-empty string and that returns a boolean
# representing whether the string is a palindrome.

def isPalindrome(string):
    # Write your code here.
	idx1 = 0
	idx2 = len(string) - 1
	
	while idx1 < idx2:
		if string[idx1] != string[idx2]:
			return False
		idx1 += 1
		idx2 -= 1 
	
	return True

assert isPalindrome('abcdcba') == True
assert isPalindrome('a') == True
assert isPalindrome('ab') == False
assert isPalindrome('aba') == True
assert isPalindrome('abb') == False
assert isPalindrome('abba') == True
assert isPalindrome('abcdefghhgfedcba') == True
assert isPalindrome('abcdefghihgfedcba') == True
assert isPalindrome('abcdefghihgfeddcba') == False

print('All tests have passed successfully')
