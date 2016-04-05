class Solution(object):
    def cleanLand(self,dp,i,j):
        if i<0 or i>len(dp)-1 or j<0 or j>len(dp[0])-1 or dp[i][j]!=1:
            return None
        dp[i][j]=0
        self.cleanLand(dp,i+1,j)
        self.cleanLand(dp,i-1,j)
        self.cleanLand(dp,i,j+1)
        self.cleanLand(dp,i,j-1)
    def numIslands(self, grid):
        
        #str to list(int)
        if grid==[]:
            return 0
        temp=[]
        for i in grid:
            temp.append(list(i))
        dp=[]
        for i in range(len(temp)):
            dp.append([])
            for j in range(len(temp[0])):
                dp[-1].append(int(temp[i][j]))
        
        
        #count
        count=0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j]==1:
                    self.cleanLand(dp,i,j)
                    count+=1
        return count
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        