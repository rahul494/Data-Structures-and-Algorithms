# AlgoExpert - Nth Fibonacci

# The Fibonacci sequence is defined as follows: the first number of the sequence
# is 0, the second number is 1, , and the nth number is the sum of the (n - 1)th
# and (n - 2)th numbers. Write a function that takes in an integer n  and returns the nth Fibonacci number.

# Important note: the Fibonacci sequence is often defined with its first two
# numbers as F0 = 0 and F1 = 1. . For the purpose of this question, the first Fibonacci number is 
# F0; therefore, getNthFib(1) is equal to F0, getNthFib(2) is equal to F1, etc...

# Sample Input #1
#    n = 2

# Sample Output #1
#    1

# Sample Input #2
#    n = 6

# Sample Output #2
#   5

def getNthFib(n):
    if(n == 1):
        return 0
    
    elif(n == 2):
        return 1

    else:
        return getNthFib(n-1) + getNthFib(n-2)

assert getNthFib(1) == 0
assert getNthFib(2) == 1
assert getNthFib(5) == 3
assert getNthFib(6) == 5

print('All tests have passed sucessfully')
