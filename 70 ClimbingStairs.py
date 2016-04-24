

#Fib
class Solution(object):
    
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        count = 3
        a, b = 1, 2
        c = 0
        while count < n + 1:
            c = a + b
            a, b = b, c
            count += 1
        return c