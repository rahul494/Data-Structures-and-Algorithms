def max_sub_array_of_size_k(k, arr):
    max_sum, curr_sum = 0, 0
    window_start = 0
    for window_end in range(len(arr)):
        curr_sum += arr[window_end]
        if window_end >= k - 1:
            if max_sum < curr_sum:
                max_sum = curr_sum
            curr_sum -= arr[window_start]
            window_start += 1

    return max_sum


# ans: 9
print("The maximum sub array of size k is " +
      str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
