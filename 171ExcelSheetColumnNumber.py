

class Solution(object)
    
    def titleToNumber(self, s)
        s = list(s)
        result = 0
        while len(s)  0
            result = 26
            result += ord(s.pop(0)) - ord('A') + 1
        return result