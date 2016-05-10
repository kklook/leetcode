# collections.OrderDict
class Solution(object):
    
    def containsNearbyDuplicate(self, nums, k):
        d = collections.OrderedDict()
        for i in range(len(nums)):
            if nums[i] in d:
                return True
            d[nums[i]] = 1
            if i >= k:
                d.popitem(last = False)
        return False