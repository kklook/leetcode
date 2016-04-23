

#找到m和n的公共前缀
class Solution(object):
    
    def rangeBitwiseAnd(self, m, n):
        count = 0
        while m != n:
            m, n = m>>1, n>>1
            count += 1
        return m << count
        