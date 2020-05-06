def bubbleSort(array):
    for i in range(len(array)):
		for j in range(len(array) - i - 1):
			if array[j] > array[j+1]:
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp

    return array

assert bubbleSort([3,4]) == [3,4]
assert bubbleSort([4, 3]) == [3,4]
assert bubbleSort([4, 3, 2]) == [2,3,4]
assert bubbleSort([4, 3, 2, 10]) == [2,3,4,10]
assert bubbleSort([4, 3, 2, 10, 12, -1, 5, 6]) == [-1,2,3,4,5,6,10,12]
assert bubbleSort([4, 3, 2, 10, 12, -1, 5, -6]) == [-6,-1,2,3,4,5,10,12]