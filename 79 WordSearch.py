# 只要做好剪枝, dfs还是可以过的
class Solution(object):
    
    def exist(self, board, word):
        
        def dfs(x, y, board, word, dp):
            if len(word) == 0:
                return True
            result = False
            for i in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                if x + i[0] < len(board) and y + i[1] < len(board[0]) and x + i[0] >= 0 and y + i[1] >= 0 and dp[x+i[0]][y+i[1]] == 0:
                    if board[x+i[0]][y+i[1]] == word[0]:
                        dp[x+i[0]][y+i[1]] = 1
                        result = result or dfs(x + i[0], y + i[1], board, word[1:], dp)
                        dp[x+i[0]][y+i[1]] = 0
            return result
        if len(word) == 0:
            return True
        result = False
        dp = [[0] * len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    dp[i][j] = 1
                    result = result or dfs(i, j, board, word[1:], dp)
                    dp[i][j] = 0
        return result