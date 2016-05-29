class Solution(object):
    
    def myPow(self, x, n):
        
        def ppow(x, n):
            if n == 1:
                return x
            t = ppow(x, n / 2)
            if n & 1:
                return t * t * x
            else:
                return t * t
                
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / ppow(x, -n)
        else:
            return ppow(x, n)