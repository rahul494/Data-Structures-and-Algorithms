class Solution:
    def numSpecial(self, mat):
        result = 0
        row_count = [0] * len(mat)
        col_count = [0] * len(mat[0])
        
        # row count
        for i in range(len(mat)):
            row_count[i] = sum(mat[i])
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    col_count[j] += 1
        
        # special number count
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                        result += 1

        return result

s = Solution()
print(s.numSpecial([[0,0],[0,0],[1,0]]))