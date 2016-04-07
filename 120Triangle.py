class Solution(object):
    
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return min(triangle[0])
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        