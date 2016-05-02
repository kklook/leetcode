

# use zfill!
# 直接模拟, leetcode真实智障!
class Solution(object):
    
    def divide(self, dividend, divisor):
        log = True
        if dividend < 0: 
            log = not log
            dividend = -dividend
        if divisor < 0:
            log = not log
            divisor = -divisor
        divb = list(str(dividend))
        result = ""
        for i in range(len(divb)):
            temp = ""
            for j in range(0, i + 1):
                temp += divb[j]
            temp = int(temp)
            count = 0
            while temp >= divisor:
                temp -= divisor
                count += 1
            result += str(count)
            temp = str(temp).zfill(i + 1)
            for j in range(0, i + 1):
                divb[j] = temp[j]
        if int(result) > 2147483647:  # 妈的智障
            if log:
                return 2147483647
            else:
                return -2147483648
        return int(result) if log else -int(result)