# Return the biggest number smaller than or equal to target
def search_floor_of_a_number(arr, target):

    if target < arr[0]:
        return -1

    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1

    return r


print(search_floor_of_a_number([4, 6, 10], 6))
print(search_floor_of_a_number([1, 3, 8, 10, 15], 12))
print(search_floor_of_a_number([4, 6, 10], 17))
print(search_floor_of_a_number([4, 6, 10], -1))
