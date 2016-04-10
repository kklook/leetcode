

class Solution(object):
    
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        secHeight = 0
        sum = 0
        while(left < right):
            if height[left] < height[right]:
                secHeight = max(secHeight, height[left])
                sum += secHeight - height[left]
                left+=1
            else:
                secHeight = max(secHeight, height[right])
                sum += secHeight - height[right]
                right-=1
        return sum