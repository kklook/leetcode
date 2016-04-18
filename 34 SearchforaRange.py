

#��һ�������ȳ��ֵڶ�����������
class Solution(object):
    
    #�ҵ�һ�γ���
    def findBegin(self, nums, target, low, high):
        if low > high: return low
        mid = low + (high - low) / 2
        if nums[mid] < target:
            return self.findBegin(nums, target, mid + 1, high)
        else:
            return self.findBegin(nums, target, low, mid - 1)
    
    #�����һ�γ���
    def findEnd(self, nums, target, low, high):
        if low > high: return high
        mid = low + (high - low) / 2
        if nums[mid] > target:
            return self.findEnd(nums, target, low, mid - 1)
        else:
            return self.findEnd(nums, target, mid + 1, high)
            
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]
        low = self.findBegin(nums, target, 0, len(nums) - 1)
        high = self.findEnd(nums, target, 0, len(nums) - 1)
        if high >= low:
            result = [low, high]
        return result