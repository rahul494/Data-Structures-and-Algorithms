def insertionSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr[:-1])):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp 

                print(arr)
    



insertionSort([4, 3, 2, 10, 12, 1, 5, 6])
