

class Solution(object):
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        if set(s) == set(t) and len(s) == len(t):
            for i in s:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            for i in t:
                if not i in d:
                    return False
                else:
                    d[i] -= 1
                    if d[i] < 0:
                        return False
            return True
        else:
            return False