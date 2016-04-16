

class Solution(object):
    
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        t = 0
        while n > 0:
            t += n & 1
            n = n >> 1
        return t == 1
                