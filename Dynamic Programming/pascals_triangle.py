class Solution:
    def generate(self, numRows):
        
        row = []

        # assume we have our top element, start building from the second level
        level = 2
        triangle = [[1], [1,1]]

        while numRows > 1:
            for i in range(level):
                if i == 0:
                    row.append(1)
                else:
                    row.append(triangle[level - 1][i] + triangle[level - 1][i - 1])

            row.append(1)
            print(row)
            level += 1
            triangle.append(row)
            row = []
            numRows -= 1

        return triangle
    
s = Solution()
# print(s.generate(5))
s.generate(5)