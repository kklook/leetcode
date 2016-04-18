

#竟然又过了
class Solution(object):
    
    #两边循环第一边计数第二遍改数
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dp = [[0]*len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i > 0 and j > 0:
                    dp[i][j] += board[i-1][j-1]
                if i > 0:
                    dp[i][j] += board[i-1][j]
                if j > 0:
                    dp[i][j] += board[i][j-1]
                if i > 0 and j < len(board[0]) - 1:
                    dp[i][j] += board[i-1][j+1]
                if j > 0 and i < len(board) - 1:
                    dp[i][j] += board[i+1][j-1]
                if j < len(board[0]) - 1:
                    dp[i][j] += board[i][j+1]
                if i < len(board) - 1:
                    dp[i][j] += board[i+1][j]
                if i < len(board) - 1 and j < len(board[0]) - 1:
                    dp[i][j] += board[i+1][j+1]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    if dp[i][j] < 2:
                        board[i][j] = 0
                    elif dp[i][j] == 2 or dp[i][j] == 3:
                        pass
                    elif dp[i][j] > 3:
                        board[i][j] = 0
                else:
                    if dp[i][j] == 3:
                        board[i][j] = 1
                    
                    