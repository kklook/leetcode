

#Ö±½ÓÄ£Äâ
class Solution(object):
    
    def getRow(self, rowIndex):
        result = [1]
        while rowIndex > 0:
            for i in range(len(result) - 1, -1, -1):
                if i > 0:
                    result[i] += result[i - 1]
            result.append(1)
            rowIndex -= 1
        return result