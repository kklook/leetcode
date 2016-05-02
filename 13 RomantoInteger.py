

#Roman
class Solution(object):
    
    def romanToInt(self, s):
        romanwisdom = [1000, 500, 100, 50, 10, 5, 1]
        romannum = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        s = list(s)
        result, i = 0, 0
        while i < len(s) - 1:
            if romannum.index(s[i]) > romannum.index(s[i+1]):
                result += romanwisdom[romannum.index(s[i+1])] - romanwisdom[romannum.index(s[i])]
                i += 1
            else:
                result += romanwisdom[romannum.index(s[i])]
            i += 1
        return result + romanwisdom[romannum.index(s[i])] if i == len(s) - 1 else result 