def missing_number(arr):
    i = 0
    while i < len(arr):
        j = arr[i]
        if arr[i] < len(arr) and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    for i in range(len(arr)):
        if i != arr[i]:
            return i


print(missing_number([4, 0, 1, 3]))
