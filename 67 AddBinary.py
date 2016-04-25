

#bin函数与int函数的使用
class Solution(object):
    
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
        