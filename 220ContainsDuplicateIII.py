# collections.OrderedDict
class Solution(object):
    
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0 or k < 1:
            return False
        d = collections.OrderedDict()
        for i in range(len(nums)):
            key = nums[i] / max(t, 1)  # nums[i] - nums[j] <= t ==> nums[i]/t - nums[j]/t <= 1
            for v in (key - 1, key, key + 1):  # nums[i]/t - nums[j]/t <= 1 means nums[i]-1 <= nums[j] <= nums[i]+1
                if v in d and abs(nums[i] - d[v]) <= t:
                    return True
            d[key] = nums[i]
            if i >= k:  # use k item control j - i <= k
                d.popitem(last = False)
        return False