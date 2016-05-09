# 有大写
class Solution(object):
    
    def reverseVowels(self, s):
        s = list(s)
        left, right = 0, len(s) - 1
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while left < right:
            if s[left] in vow and s[right] in vow:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif not s[left] in vow:
                left += 1
            elif not s[right] in vow:
                right -= 1
        return "".join(s)