

#dfs穷举, 但这个太难写了
class Solution(object):
    
    def addOperators(self, num, target):
        
        #这个dfs我真自己写不出来
        def dfs(num, target, exp = '', mulval = 1):
            ans = []
            if num.startswith('00') or int(num) and num.startswith('0'):
                pass
            elif int(num) * mulval == target: #可以将乘法和初始情况一起解决， 很聪明
                ans += str(num) + exp,
            for i in range(len(num) - 1): #这里和下一行处理很有趣， 避免出现空串
                left, right = num[: i + 1], num[i + 1: ]
                if right.startswith('00') or int(right) and right.startswith('0'): #因为dfs开始已经判断过left
                    continue
                right, rightval = right + exp, int(right) * mulval #这里同样需要考虑乘法情况
                
                for l in dfs(left, target - rightval):
                    ans += l + '+' + right,
                for l in dfs(left, target + rightval):
                    ans += l + '-' + right,
                for l in dfs(left, target, '*' + right, rightval): #乘法的处理
                    ans += l, 
            return ans
        if not num:
            return []
        return dfs(num, target)