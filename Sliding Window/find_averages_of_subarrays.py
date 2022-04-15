def find_averages_of_subarrays(k, arr):
    subarray = []
    running_sum = 0.0
    low = 0

    for end in range(len(arr)):
        running_sum += arr[end]

        if end - low + 1 > k:
            running_sum -= arr[low]
            subarray.append(running_sum / k)
            low += 1

    return subarray

print(find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))