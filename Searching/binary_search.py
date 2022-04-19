def binary_search(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
    return -1


print(binary_search([-1, 0, 3, 5, 9, 12], 12))
