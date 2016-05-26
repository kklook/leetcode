# dfs 回溯
class Solution(object):
    
    def solveNQueens(self, n):
        dp = [[0] * n for i in range(n)]
        solution = [['.'] * n for i in range(n)]
        result = []
        def dfs(i):
            if i == n:
                t = []
                for i in solution:  # 注意格式
                    t.append("".join(i))
                result.append(t)
                return None
            for j in range(n):
                if dp[i][j] == 0:
                    for k in range(n):  # 小心重叠或漏计
                        dp[i][k] += 1
                        dp[k][j] += 1
                        if i + k < n and j + k < n and k != 0:
                            dp[i+k][j+k] += 1
                        if i - k >= 0 and j - k >= 0 and k != 0:
                            dp[i-k][j-k] += 1
                        if i + k < n and j - k >= 0 and k != 0:
                            dp[i+k][j-k] += 1
                        if i - k >= 0 and j + k < n and k != 0:
                            dp[i-k][j+k] += 1
                    solution[i][j] = 'Q'
                    dfs(i + 1)
                    for k in range(n):
                        dp[i][k] -= 1
                        dp[k][j] -= 1
                        if i + k < n and j + k < n and k != 0:
                            dp[i+k][j+k] -= 1
                        if i - k >= 0 and j - k >= 0 and k != 0:
                            dp[i-k][j-k] -= 1
                        if i + k < n and j - k >= 0 and k != 0:
                            dp[i+k][j-k] -= 1
                        if i - k >= 0 and j + k < n and k != 0:
                            dp[i-k][j+k] -= 1
                    solution[i][j] = '.'
        dfs(0)
        return result