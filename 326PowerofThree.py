

#9¸ö0
class Solution(object):
    
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        result = math.log(n) / math.log(3)
        if abs(result - round(result)) < 0.0000000001:
            return True
        else:
            return False