def largestNumber(nums) -> str:
    print(''.join(sorted(list(map(str, nums)))[::-1])) 

def main():
    largestNumber([1,61,9,0])

main()