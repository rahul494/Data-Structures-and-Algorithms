# AlgoExpert - Bubble Sort

# Write a function that takes in an array of integers and returns a sorted
# version of that array. Use the Bubble Sort algorithm to sort the array.


# If you're unfamiliar with Bubble Sort, we recommend watching the Conceptual
# Overview section of this question's video explanation before starting to code.

# Sample Input

#     array = [8, 5, 2, 9, 5, 6, 3]

# Sample Output

#     [2, 3, 5, 5, 6, 8, 9]

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    return array


assert bubbleSort([3, 4]) == [3, 4]
assert bubbleSort([4, 3]) == [3, 4]
assert bubbleSort([4, 3, 2]) == [2, 3, 4]
assert bubbleSort([4, 3, 2, 10]) == [2, 3, 4, 10]
assert bubbleSort([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
assert bubbleSort([4, 3, 2, 10, 12, -1, 5, 6]) == [-1, 2, 3, 4, 5, 6, 10, 12]
assert bubbleSort([4, 3, 2, 10, 12, -1, 5, -6]) == [-6, -1, 2, 3, 4, 5, 10, 12]
assert bubbleSort([114, 3, 291, 10, -1, 9999, -6]) == [-6, -1, 3, 10, 114, 291, 9999]

print('All tests have passed successfully')
