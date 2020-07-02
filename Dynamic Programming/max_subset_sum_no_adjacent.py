 # AlgoExpert - Max Subset Sum No Adjacent
 
#   Write a function that takes in an array of positive integers and returns the
#   maximum sum of non-adjacent elements in the array.
#   If a sum can't be generated, the function should return 0

#   Sample Input

#     array = [75, 105, 120, 75, 90, 135]

#   Output

#     330 (75 + 120 + 135) 

def maxSubsetSumNoAdjacent(array):

    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]

    second = array[0]
    first = max(array[0], array[1])

    for i in range(2, len(array)):
        curr = max(first, second + array[i])
        second = first
        first = curr

    return first

assert maxSubsetSumNoAdjacent([7, 10, 12, 7, 9, 14]) == 33
assert maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]) == 330
assert maxSubsetSumNoAdjacent([]) == 0
assert maxSubsetSumNoAdjacent([1]) == 1
assert maxSubsetSumNoAdjacent([1, 2]) == 2

print('All tests have passed successfully')