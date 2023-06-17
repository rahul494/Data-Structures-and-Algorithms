class SubrectangleQueries:

    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for j in range(row1, row2 + 1):
            for i in range(col1, col2 + 1):
                self.rectangle[j][i] = newValue
        
    def getValue(self, row, col):
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
rectangle = [[1,2,1],[4,3,4],[3,2,1],[1,1,1]]
obj = SubrectangleQueries(rectangle)
print(obj.getValue(0, 2))
obj.updateSubrectangle(0, 0, 3, 2, 5)
print(obj.rectangle)
print(obj.getValue(0, 2))