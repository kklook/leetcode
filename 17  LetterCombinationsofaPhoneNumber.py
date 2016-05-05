

# 确实不会使itertools, 直接递归
class Solution(object):
    
    def letterCombinations(self, digits):
        digits = list(digits)
        if len(digits) == 0:
            return []
        valueMap = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        if len(digits) > 1:
            result = self.letterCombinations("".join(digits[:-1]))
        else:
            return list(valueMap[digits[0]])
        key = digits[-1]
        value = []
        if key in valueMap:
            value = valueMap[key]
            value = list(value)
        n = len(result)
        newresult = []
        for i in range(n):
            newresult.extend(value)
        for i in range(len(result)):
            for j in range(len(value)):
                newresult[i * len(value) + j] = result[i] + newresult[i * len(value) + j]
        return newresult