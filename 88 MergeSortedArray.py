# n + m = len(nums1) 蛋疼
class Solution(object):
    
    def merge(self, nums1, m, nums2, n):
        for i in range(m - 1, -1, -1):
            nums1[i+n] = nums1[i]
        i, j = n, 0
        k = 0;
        while i < n + m and j < n:
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        if j < n:
            while j < n:
                nums1[k] = nums2[j]
                k += 1
                j += 1