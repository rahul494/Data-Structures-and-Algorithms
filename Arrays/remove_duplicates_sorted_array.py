def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]) == 4)
    print(remove_duplicates([2, 2, 2, 11]) == 2)
    print(remove_duplicates([]) == 0)
    print(remove_duplicates([2]) == 1)
    print(remove_duplicates([2, 2, 2]) == 1)

def remove_duplicates(arr):
    l, r, unique_length = 0, 0, 0

    while r < len(arr):
        if arr[l] == arr[r] and l == r:
            # covers first step
            unique_length += 1
        elif arr[l] == arr[r]:
            # we are at a duplicate number
            l = r
        else:
            # we found a new unique number
            unique_length += 1
            l = r
        r += 1

    return unique_length

if __name__ == '__main__':
    main()