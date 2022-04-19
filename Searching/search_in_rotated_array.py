def search_in_rotated_array(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == arr[mid]:
            return mid

        # left sorted portion
        if arr[l] <= arr[mid]:
            if target > arr[mid] or target < arr[l]:
                l = mid + 1
            else:
                r = mid - 1        
                
        # right sorted portion
        else:
            if target < arr[mid] or target > arr[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1


print(search_in_rotated_array([4, 5, 6, 7, 0, 1, 2], 0))  # 4
print(search_in_rotated_array([4, 5, 6, 7, 0, 1, 2], 3))  # -1
