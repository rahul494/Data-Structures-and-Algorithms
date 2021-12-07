def find_averages_of_subarrays_naive(k, arr):
    result = []
    for i in range(len(arr) - k + 1):
        sum = 0.0
        for j in range(i, i+k):
            sum += arr[j]
        result.append(sum/5)

    return result


def find_averages_of_subarrays(k, arr):
    result = []
    window_sum = 0.0
    window_start = 0
    for i in range(len(arr) - k + 1):
        sum = 0.0
        for j in range(i, i+k):
            sum += arr[j]
        result.append(sum/5)

    return result


def main():
    result = find_averages_of_subarrays_naive(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
