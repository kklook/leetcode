# 栈的使用
class Solution(object):
    
    def isValid(self, s):
        result = ['#']
        s = list(s)
        while len(s) > 0:
            t = s.pop(0)
            if (t == ')' and result[-1] != '(')\
                or (t == '}' and result[-1] != '{')\
                or (t == ']' and result[-1] != '['):
                return False
            elif t == ')' or t == '}' or t == ']':
                result.pop()
            else:
                result.append(t)
        if len(result) == 1:
            return True
        else:
            return Falses