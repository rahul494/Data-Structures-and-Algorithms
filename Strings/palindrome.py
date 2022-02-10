# AlgoExpert - Palindrome Check

# A palindrome is defined as a string that's written the same forward and
# backward. Note that single-character strings are palindromes.

# Write a function that takes in a non-empty string and that returns a boolean
# representing whether the string is a palindrome.

# Sample Input

# 	string = "abcdcba"

# Sample Output

# 	true

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

def checkPotentialPalindrom(cAr, start, end, altcnt):
       if end <= start:
             return True

       if cAr[start] != cAr[end]:
            altcnt = altcnt + 1

       if altcnt > 1:
             return False

       return checkPotentialPalindrom(cAr, start + 1, end - 1, altcnt)

def recursive_pal(str):
	if len(str) <= 1:
		print('this is a palindrome')
		return True
	elif str[0] == str[len(str)-1]:
		recursive_pal(str[1:len(str)-1])
	else:
		return False
		
assert isPalindrome('abcdcba') == True
assert isPalindrome('a') == True
assert isPalindrome('ab') == False
assert isPalindrome('aba') == True
assert isPalindrome('abb') == False
assert isPalindrome('abba') == True
assert isPalindrome('abcdefghhgfedcba') == True
assert isPalindrome('abcdefghihgfedcba') == True
assert isPalindrome('abcdefghihgfeddcba') == False
assert checkPotentialPalindrom('abcdcba', 0, 6, 0) == True
assert recursive_pal('abcdcba') == False

print('All tests have passed successfully')
