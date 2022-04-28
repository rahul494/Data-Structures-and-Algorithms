def square_array(arr):
    result = []
    i, l, r = 0, 0, len(arr) - 1

    while i < len(arr):
        if abs(arr[l]) > abs(arr[r]):
            result.insert(0, arr[l] * arr[l])
            l += 1
        else:
            result.insert(0, arr[r] * arr[r])
            r -= 1
        i += 1

    return result

# NOTE: double check grokking solution, their solution looks over engineered?

def main():
    print(square_array([-2, -1, 0, 1, 2]) == [0, 1, 1, 4, 4])
    print(square_array([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9])
    print(square_array([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9])
    print(square_array([-1, -1, -1, -1, -1]) == [1, 1, 1, 1, 1])
    print(square_array([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0])
    print(square_array([]) == [])

if __name__ == '__main__':
    main()