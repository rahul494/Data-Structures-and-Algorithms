class Solution:
    def getLucky(self, s: str, k: int) -> int:
        conversions = []

        for letter in s:
            conversions.append(str(ord(letter) - 96))
        
        result = ''.join(conversions)
        transform_1 = 0

        for num in result:
            transform_1 += int(num)
        
        if k == 1:
            return transform_1
        else:
            transform_2 = 0
            while transform_1 > 0:
                transform_2 += transform_1 % 10
                transform_1 //= 10
            
            return transform_2

s = Solution()
print(s.getLucky("qhquvppzooyt", 2))