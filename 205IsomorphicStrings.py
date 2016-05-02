

#use get!
class Solution(object):
    
    def isIsomorphic(self, s, t):
        db = {}
        da = {}
        for i in range(len(s)):
            if not s[i] in db and not t[i] in da:
                db[s[i]] = t[i]
                da[t[i]] = s[i]
            else:
                if db.get(s[i]) != t[i] or da.get(t[i]) != s[i]:
                    return False
        return True