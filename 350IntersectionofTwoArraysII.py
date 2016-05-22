class Solution(object):
    
    def intersect(self, nums1, nums2):
        result = []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        counter = collections.Counter(nums1)
        for i in nums2:
            if counter[i] > 0:
                result.append(i)
                counter[i] -= 1
        return result