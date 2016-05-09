class Solution(object):
    
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        while len(v1) >= 1 and int(v1[-1]) == 0:
            v1.pop()
        while len(v2) >= 1 and int(v2[-1]) == 0:
            v2.pop()
        for i in range(min(len(v1), len(v2))):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        if len(v1) == len(v2):
            return 0
        else:
            return 1 if len(v1) > len(v2) else -1