

class Solution(object):
    
    def isPowerOfFour(self, num):
        if num <= 0:
            return False
        result = math.log(num) / math.log(4)
        if abs(result - round(result)) < 0.0000000001:
            return True
        else:
            return False