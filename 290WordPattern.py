

# use split!
class Solution(object):
    
    def wordPattern(self, pattern, str):
        str = str.split()
        da = {}
        db = {}
        if not len(str) == len(pattern):
            return False
        for i in range(len(pattern)):
            before = db.get(pattern[i])
            after = da.get(str[i])
            if before == None and after == None:
                db[pattern[i]] = str[i]
                da[str[i]] = pattern[i]
            else:
                if not before == str[i] or not after == pattern[i]:
                    return False
        return True