

class Solution(object):
    
    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return []
        d = {}
        result = []
        for i in strs:
            s = ''.join(sorted(i))
            if s in d:
                d[s] += [i]
            else:
                d[s] = [i]
        for i in d:
            d[i].sort()
            result += [d[i]]
        return result
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """