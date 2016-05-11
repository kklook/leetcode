class Solution(object):
    
    def isHappy(self, n):
        s = set()
        while n != 1 and not n in s:
            s.add(n)
            t = 0
            while n:
                t += (n % 10) * (n % 10)
                n /= 10
            n = t
        if n == 1:
            return True
        else:
            return False