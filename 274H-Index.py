

# 欺负我数学不好, 怒递归之!
class Solution(object):
    
    def hIndex(self, citations):
        if len(citations) == 0:
            return 0
        if len(citations) <= min(citations):
            return len(citations)
        citations.pop(citations.index(min(citations)))
        return self.hIndex(citations)