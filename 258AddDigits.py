class Solution(object):
    
    def addDigits(self, num):
        while num / 10 > 0:
            t = 0
            while num:
                t += num % 10
                num /= 10
            num = t
        return num