class Solution(object):
    
    def topKFrequent(self, nums, k):
        c = collections.Counter(nums)
        return [x[0] for x in c.most_common(k)]