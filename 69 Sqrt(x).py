# 牛顿迭代
class Solution(object):
    
    def mySqrt(self, x):
        t = x
        while t * t > x:
            t = (t + x / t) / 2
        return t