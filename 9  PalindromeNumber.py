# 确实没有有名的额外空间, 什么你说无名, 我不知道!
class Solution(object):
    
    def isPalindrome(self, x):
        return x == int("".join(list(reversed(list(str(x)))))) if x >= 0 else False