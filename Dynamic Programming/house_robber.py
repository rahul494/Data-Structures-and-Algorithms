def house_robber(houses):
    if len(houses) <= 2:
        return max(houses)

    houses[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        houses[i] = max(houses[i - 1], houses[i-2] + houses[i])

    return houses[-1]

print(house_robber([1,2,3,1])) # 4