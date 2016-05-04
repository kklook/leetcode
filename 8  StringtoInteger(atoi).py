

class Solution(object):
    
    def myAtoi(self, str):
        if len(str) == 0:
            return 0
        i = 0
        while i < len(str) - 1 and str[i].isspace():
            i += 1
        sign = str[i]
        if sign == '-' or sign == '+':
            i += 1
        result = 0
        while i < len(str):
            number = str[i]
            if ord(number) >= ord('0') and ord(number) <= ord('9'):
                result *= 10
                result += ord(number) - ord('0')
            else:
                break
            i += 1
        if sign == '-':
            result = -result
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result