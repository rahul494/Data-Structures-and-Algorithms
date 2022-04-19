def find_max_in_bitonic_array(arr):
    l, r, = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] > arr[m + 1]:
            r = m
        else:
            l = m + 1

    return arr[l]


print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))  # 12
print(find_max_in_bitonic_array([3, 8, 3, 1]))  # 8
print(find_max_in_bitonic_array([1, 3, 8, 12]))  # 12
print(find_max_in_bitonic_array([10, 9, 8]))  # 10