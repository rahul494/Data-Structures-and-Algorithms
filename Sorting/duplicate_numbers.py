def duplicate_numbers(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    duplicates = []

    for i in range(len(arr)):
        if arr[i] != i + 1:
            duplicates.append(arr[i])
    
    return duplicates

print(duplicate_numbers([5, 4, 3, 4, 5]))
