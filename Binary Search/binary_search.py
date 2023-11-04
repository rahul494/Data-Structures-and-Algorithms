def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    mid = l + ((r - l) // 2)

    while l <= r:
        mid = l + ((r - l) // 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1

    return -1

print(binary_search([1,3,6,9,13,16,18], 6))
