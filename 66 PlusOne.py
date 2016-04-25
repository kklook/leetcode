

class Solution(object):
    
    def dfs(self, digits, i):
        t = 0
        if i < len(digits) - 1:
            t = self.dfs(digits, i + 1)
        else:
            t = 1
        count = digits[i] + t
        digits[i] = count % 10
        return count / 10
    def plusOne(self, digits):
        i = self.dfs(digits, 0)
        if i == 1:
            digits = [1] + digits
        return digits