

# dfs
class Solution(object):
    
    def combinationSum(self, candidates, target):
        self.result = []
        def istarget(candidates, target, result, t):
            if target == 0:
                result.sort()
                self.result.append(result)
            if target > 0:
                for i in range(t, len(candidates)):
                    istarget(candidates, target - candidates[i], [candidates[i]] + result, i)  # 每次从上一次i开始防止重复
        istarget(candidates, target, [], 0)
        self.result.sort()
        return self.result