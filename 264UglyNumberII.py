class Solution(object):
    
    def nthUglyNumber(self, n):
        result = [1]
        u2 = u3 = u5 = 0
        while len(result) < n:
            min2, min3, min5 = result[u2] * 2, result[u3] * 3, result[u5] * 5
            m = min(min2, min3, min5)
            if m == min2:
                u2 += 1
            if m == min3:
                u3 += 1
            if m == min5:
                u5 += 1
            result.append(m)
        return result[-1]