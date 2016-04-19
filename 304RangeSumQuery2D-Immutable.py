

#先求出每行和列表, 再逐行加和给出结果
class NumMatrix(object):
    
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.resultList = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            self.resultList[i][0] = matrix[i][0]
            for j in range(1, len(matrix[0])):
                self.resultList[i][j] = self.resultList[i][j - 1] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        result = 0
        for i in range(row1, row2 + 1):
            if col1 == 0:
                result += self.resultList[i][col2]
            else:
                result += self.resultList[i][col2] - self.resultList[i][col1 - 1]
        return result