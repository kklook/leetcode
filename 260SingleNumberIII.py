

class Solution(object):
    
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        result = []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in nums:
            if d[i] == 1:
                result.append(i)
        return result
                