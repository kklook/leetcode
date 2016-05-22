class Solution(object):
    
    def intersection(self, nums1, nums2):
        counter = collections.Counter(nums1)
        result = []
        for i in nums2:
            if counter[i] > 0:
                result.append(i)
                counter[i] = 0
        return result