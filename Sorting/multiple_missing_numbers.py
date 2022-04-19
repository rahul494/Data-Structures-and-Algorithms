def missing_numbers(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        # if the value does not map correctly do its index, preform swap
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    result = []

    for i in range(len(arr)):
        if arr[i] != i + 1:
            result.append(i + 1)

    return result

print(missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))