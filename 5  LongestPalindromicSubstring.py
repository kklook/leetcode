

#dp³¬Ê±°¡
class Solution(object):
    
    def longestPalindrome(self, s):
        
        def part(s, left, right):
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left, right = left - 1, right + 1
            return s[left + 1: right]
        
        result = ""
        for i in range(len(s)):
            t = part(s, i, i)
            if len(result) < len(t):
                result = t[:]
            t = part(s, i, i+1)
            if len(result) < len(t):
                result = t[:]
        return result