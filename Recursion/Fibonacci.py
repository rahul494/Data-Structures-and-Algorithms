def getNthFibRec(n):
    if(n == 1):
        return 1
    
    elif(n == 2):
        return 1

    else:
        return getNthFibRec(n-1) + getNthFibRec(n-2)

def getNthFibIter(n):
    lastTwo = [1,1]
    
    while(n >= 3):
        n = n - 1
        temp = lastTwo[0]
        lastTwo[0] =  lastTwo[1]
        lastTwo[1] = lastTwo[1] + temp

    return lastTwo[1] if n > 1 else lastTwo[0]

assert getNthFibRec(1) == 1
assert getNthFibIter(1) == 1
assert getNthFibRec(6) == 8
assert getNthFibIter(6) == 8

print('All tests have passed sucessfully')