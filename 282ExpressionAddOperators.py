

#dfs���, �����̫��д��
class Solution(object):
    
    def addOperators(self, num, target):
        
        #���dfs�����Լ�д������
        def dfs(num, target, exp = '', mulval = 1):
            ans = []
            if num.startswith('00') or int(num) and num.startswith('0'):
                pass
            elif int(num) * mulval == target: #���Խ��˷��ͳ�ʼ���һ������ �ܴ���
                ans += str(num) + exp,
            for i in range(len(num) - 1): #�������һ�д������Ȥ�� ������ֿմ�
                left, right = num[: i + 1], num[i + 1: ]
                if right.startswith('00') or int(right) and right.startswith('0'): #��Ϊdfs��ʼ�Ѿ��жϹ�left
                    continue
                right, rightval = right + exp, int(right) * mulval #����ͬ����Ҫ���ǳ˷����
                
                for l in dfs(left, target - rightval):
                    ans += l + '+' + right,
                for l in dfs(left, target + rightval):
                    ans += l + '-' + right,
                for l in dfs(left, target, '*' + right, rightval): #�˷��Ĵ���
                    ans += l, 
            return ans
        if not num:
            return []
        return dfs(num, target)