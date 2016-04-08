

class Solution(object):
    
    def isAdditiveNumber(self, num):
        n = len(num)
        for i, j in itertools.combinations(range(1, n), 2):
            a, b = num[:i], num[i:j]
            if a + b == str(int(a)) + str(int(b)):
                while j < n:
                    c = str(int(a) + int(b))
                    if not num.startswith(c, j):
                        break
                    j += len(c)
                    a, b = b, c
                    if j == n:
                        return True
        return False
        
        """
        :type num: str
        :rtype: bool
        """