

class Solution(object):
    
    def reverse(self, x):
        log = 1
        if x < 0:
            x = -x
            log = -1
        x = list(str(x))
        x.reverse()
        return int("".join(x)) * log if int("".join(x)) < 2147483647 and int("".join(x)) > -2147483648 else 0