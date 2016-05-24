class Solution(object):
    
    def permuteUnique(self, nums):
        result = [[]]
        for n in nums:
            temp = []
            for ret in result:
                for i in range(len(ret) + 1):
                    temp += ret[:i] + [n] + ret[i:],
                    if i < len(ret) and ret[i] == n:  # 相同者直插入一遍
                        break
            result = temp
        return result