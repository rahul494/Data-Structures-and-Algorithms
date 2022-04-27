def sorted_2sum(arr, target):
    l, r = 0, len(arr) - 1

    while l < r:
        curr_sum = arr[l] + arr[r]

        if curr_sum == target:
            return [l, r]
        elif curr_sum > target:
            r -= 1
        else:
            l += 1
    
    return [-1, -1]

def main():
    print(sorted_2sum([1, 2, 3, 4, 6], 6) == [1,3])
    print(sorted_2sum([2, 5, 9, 11], 11) == [0,2])
    print(sorted_2sum([2, 5, 9, 11], 5) == [-1,-1])
    
if __name__ == '__main__':
    main()