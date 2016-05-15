# 用一个大根和一个小根堆来分割数组
class MedianFinder:
    
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        
    def addNum(self, num):
        heapq.heappush(self.maxHeap, -num)
        left = self.maxHeap[0] 
        right = self.minHeap[0] if len(self.minHeap) else None
        if right < -left or len(self.minHeap) + 1 < len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        
    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        else:
            return -1.0 * self.maxHeap[0]