

# Roman
class Solution(object):
    
    def intToRoman(self, num):
        result = ""
        romanwisdom = [1000, 500, 100, 50, 10, 5, 1]
        romannum = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        number = 1000
        while num:
            t = num / number
            if t > 0 and t < 4:
                for i in range(t):
                    result += romannum[romanwisdom.index(number)]
            elif t == 4:
                result += romannum[romanwisdom.index(number)]
                result += romannum[romanwisdom.index(number) - 1]
            elif t == 5:
                result += romannum[romanwisdom.index(number) - 1]
            elif t > 5 and t < 9:
                result += romannum[romanwisdom.index(number) - 1]
                for i in range(t - 5):
                    result += romannum[romanwisdom.index(number)]
            elif t == 9:
                result += romannum[romanwisdom.index(number)]
                result += romannum[romanwisdom.index(number) - 2]
            num %= number
            number /= 10
        return result