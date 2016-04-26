

#dfs
class Solution(object):
    
    def dfs(self, result, i, numRows):
        if i == numRows:
            return result
        if i == 0:
            return self.dfs([[1]], i + 1, numRows)
        result.append([])
        for j in range(i + 1):
            if j > 0 and j < i:
                result[-1] += [result[i - 1][j - 1] + result[i - 1][j]]
            else:
                result[-1] += [1]
        return self.dfs(result, i + 1, numRows)
        
    def generate(self, numRows):
        if numRows > 0:
            return self.dfs([], 0, numRows)
        else:
            return []