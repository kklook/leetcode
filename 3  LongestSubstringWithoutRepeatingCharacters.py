# 最后要再多算一遍
class Solution(object):
    
    def lengthOfLongestSubstring(self, s):
        resultList = []
        result = 0
        for i in s:
            if i in resultList:
                result = max(result, len(resultList))
                resultList = resultList[resultList.index(i)+1:]
            resultList.append(i)
        result = max(result, len(resultList))
        return result