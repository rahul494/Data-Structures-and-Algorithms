def order_agnostic_binary_search(arr, target):
    l, r = 0, len(arr) - 1
    is_ascending = arr[l] < arr[r]
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif is_ascending:
            if arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        else:
            if arr[m] < target:
                r = m - 1
            else:
                l = m + 1


print(order_agnostic_binary_search([4, 6, 10], 10))  # 2
print(order_agnostic_binary_search([1, 2, 3, 4, 5, 6, 7], 5))  # 4
print(order_agnostic_binary_search([7, 6, 5, 4, 3, 2, 1], 5))  # 2
print(order_agnostic_binary_search([10, 6, 4], 10))  # 0
print(order_agnostic_binary_search([10, 6, 4], 4))  # 2
