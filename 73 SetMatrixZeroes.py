

#好土的算法竟然过了
class Solution(object):
    
    #直接2次循环一次记录位置第二次清零
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        record = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i in record:
                        record[i].append(j)
                    else:
                        record[i] = [j]
        for i in record:
            matrix[i] = [0 for t in range(len(matrix[0]))]
            for j in range(len(record[i])):
                for t in range(len(matrix)):
                    matrix[t][record[i][j]] = 0
        