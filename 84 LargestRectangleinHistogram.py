

#利用栈结构构建一个当前元素下的矩形高度栈
#原理:递增高度队列下第i个高度最大值为
#h[i] = heights[i] * (len(heights[i]) - i)
#所以我们只要构造一个当前元素下的递增高度栈即可
class Solution(object):
    
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        resultList = []
        result = 0
        for i in heights:
            if len(resultList) == 0:
                resultList.append(i)
            else:
                count = 1
                while len(resultList) > 0 and resultList[-1] > i: #计算块面积
                    result = max(resultList.pop() * count, result)
                    count += 1
                while count > 0: #重新填充当前最小块的高度
                    resultList.append(i)
                    count -= 1
        count = 1
        while(len(resultList) > 0):
            result = max(resultList.pop() * count, result)
            count += 1
        return result
                    