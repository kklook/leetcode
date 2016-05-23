# 炫酷！
class Solution(object):
    
    def minWindow(self, s, t):
        count, need = collections.Counter(t), len(t)
        i = ir = jr = 0
        for j, c in enumerate(s, 1):  # j从1开始代表if下面已经处理过c了
            need -= count[c] > 0
            count[c] -= 1
            if not need:
                while i < j and count[s[i]] < 0:  # 炫酷！
                    count[s[i]] += 1
                    i += 1
                if jr == 0 or j - i <= jr - ir:
                    ir, jr = i, j
        return s[ir:jr]