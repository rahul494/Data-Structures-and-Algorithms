def getNthFib(n):
    if(n == 1):
        return 1
    
    elif(n == 2):
        return 1

    else:
        return getNthFib(n-1) + getNthFib(n-2)

print(getNthFib(6))