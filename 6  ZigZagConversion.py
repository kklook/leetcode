

#���Ǻܶ�������������㷨
class Solution(object):
    
    def convert(self, s, numRows):
        if numRows >= len(s) or numRows == 1:
            return s
        s = list(s)
        resultList = []
        for i in range(numRows):
            j = i
            while j < len(s):
                resultList.append(s[j])
                if i > 0 and i < numRows - 1 and j + (numRows - i) * 2 - 2 < len(s):
                    resultList.append(s[j + (numRows - i) * 2 - 2])
                j += (numRows - 1) * 2
        return "".join(resultList)