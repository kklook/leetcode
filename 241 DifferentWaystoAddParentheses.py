# 分之左右，split要带括号！
class Solution(object):
    
    def diffWaysToCompute(self, input):
        def calc(l, r, o):
            return {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}[o](l, r)
        def dfs(num, ops):
            if not ops:
                return num[0],
            ans = []
            for x in range(len(ops)):
                left = dfs(num[:x+1], ops[:x])
                right = dfs(num[x+1:], ops[x+1:])
                for l in left:
                    for r in right:
                        ans.append(calc(l, r, ops[x]))
            return ans
        ops = []
        num = []
        input = re.split(r'(\D)', input)
        for i in input:
            if i.isdigit():
                num.append(int(i))
            else:
                ops.append(i)
        return dfs(num, ops)