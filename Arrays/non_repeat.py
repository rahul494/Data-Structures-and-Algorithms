def non_repeat(input_list):
    hist = {}
    nonrep = []

    for ele in input_list:
        if ele in hist:
            hist[ele] += 1
        else:
            hist[ele] = 1

    for key in hist:
        if hist[key] == 1:
            nonrep.append(key)

    return nonrep


print(non_repeat([1, 2, 3, 2, 4, 1, 4, 5]))

# time taken -> linear time
# space taken -> linear space
