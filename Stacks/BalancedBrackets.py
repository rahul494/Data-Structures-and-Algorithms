# AlgoExpert - Balanced Brackets

# Write a function that takes in a string made up of brackets '(', '{', '[', ')', '}', ']'
# and other optional characters. The function should return a
# boolean representing whether the string is balanced with regards to brackets.


# A string is said to be balanced if it has as many opening brackets of a
# certain type as it has closing brackets of that type and if no bracket is
# unmatched. Note that an opening bracket can't match a corresponding closing
# bracket that comes before it, and similarly, a closing bracket can't match a
# corresponding opening bracket that comes after it. Also, brackets can't
# overlap each other as in '[(])'

# Sample Input:

#     string = "([])(){}(())()()"

# Sample Output: 

#     true
  
def balancedBrackets(string):
    stack = []
    openingBracket = ['(', '{', '[']
    closingBracket = [')', '}', ']']

    for bracket in string:
        if bracket in openingBracket:
            stack.append(bracket)
        elif bracket in closingBracket:
            if len(stack) == 0:
                return False
            if openingBracket.index(stack[-1]) == closingBracket.index(bracket):
                del stack[-1]
            else:
                return False

    return stack == []


assert balancedBrackets(r'([])(){}(())()()') == True
assert balancedBrackets(r'()[]{}{') == False
assert balancedBrackets(r'(((((({{{{{[[[[[([)])]]]]]}}}}}))))))') == False
assert balancedBrackets(r'()()[{()})]') == False
assert balancedBrackets(r'(()())((()()()))') == True
assert balancedBrackets(r'{}()') == True
assert balancedBrackets(r'()([])') == True
assert balancedBrackets(r'((){{{{[]}}}})') == True

print('All tests have passed successfully')