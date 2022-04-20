# O(n) space
def run_length_encoding(arr):
    result = [arr[0]]
    for ele in arr:
        if ele != result[-1]:
            result.append(ele)

    return result

# O(1) space
def run_length_encoding_2(arr):
    i = 1
    while i < len(arr):
        if arr[i] == arr[i - 1]:
            del arr[i]
            i -= 1
        i += 1
    
    return arr
        

print(run_length_encoding([0,0,1,1,1,2,3,4,4]))
print(run_length_encoding_2([0,0,1,1,1,2,3,4,4]))