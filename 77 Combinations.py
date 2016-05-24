class Solution(object):
    
    def combine(self, n, k):
        return list(itertools.combinations(range(1, n + 1), k))