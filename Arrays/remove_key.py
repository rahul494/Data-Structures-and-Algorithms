def remove_key(arr, key):
    no_keys_length = 0

    for ele in arr:
        if ele != key:
            no_keys_length += 1

    return no_keys_length

def remove_key_2(arr, key):
    next_element = 0

    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_element] = arr[i]
            next_element += 1

    return next_element

def main():
    print(remove_key([3, 2, 3, 6, 3, 10, 9, 3], 3) == 4)
    print(remove_key([2, 11, 2, 2, 1], 2) == 2)
    print(remove_key([], 2) == 0)
    print(remove_key([1], 2) == 1)
    print(remove_key([2], 2) == 0)
    print('-----------------')
    print(remove_key_2([3, 2, 3, 6, 3, 10, 9, 3], 3) == 4)
    print(remove_key_2([2, 11, 2, 2, 1], 2) == 2)
    print(remove_key_2([], 2) == 0)
    print(remove_key_2([1], 2) == 1)
    print(remove_key_2([2], 2) == 0)
    

if __name__ == '__main__':
    main()