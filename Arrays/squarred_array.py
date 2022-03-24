def squarred_array(array):
    
    res = []
    l, r = 0, len(array) - 1

    while l <= r:
        if abs(array[l]) > abs(array[r]):
            res.append(array[l] * array[l])
            l += 1
        else:
            res.append(array[r] * array[r])
            r -= 1

    return res


print(squarred_array([-4, -1, 0, 3, 3, 10]))