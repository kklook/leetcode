# 这题有坑！
class Solution(object):
    
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return matrix
        i, j = 0, 0
        tot = 1
        length = len(matrix) * len(matrix[0])
        result = []
        result.append(matrix[0][0])
        while tot < length:
            while j < len(matrix[0]) - 1 and matrix[i][j+1] != sys.maxint:
                matrix[i][j] = sys.maxint
                j += 1
                tot += 1
                result.append(matrix[i][j])
            while i < len(matrix) - 1 and matrix[i+1][j] != sys.maxint:
                matrix[i][j] = sys.maxint
                i += 1
                tot += 1
                result.append(matrix[i][j])
            while j > 0 and matrix[i][j-1] != sys.maxint:
                matrix[i][j] = sys.maxint
                j -= 1
                tot += 1
                result.append(matrix[i][j])
            while i > 0 and matrix[i-1][j] != sys.maxint:
                matrix[i][j] = sys.maxint
                i -= 1
                tot += 1
                result.append(matrix[i][j])
        return result