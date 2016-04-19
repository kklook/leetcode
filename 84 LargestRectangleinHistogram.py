

#����ջ�ṹ����һ����ǰԪ���µľ��θ߶�ջ
#ԭ��:�����߶ȶ����µ�i���߶����ֵΪ
#h[i] = heights[i] * (len(heights[i]) - i)
#��������ֻҪ����һ����ǰԪ���µĵ����߶�ջ����
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
                while len(resultList) > 0 and resultList[-1] > i: #��������
                    result = max(resultList.pop() * count, result)
                    count += 1
                while count > 0: #������䵱ǰ��С��ĸ߶�
                    resultList.append(i)
                    count -= 1
        count = 1
        while(len(resultList) > 0):
            result = max(resultList.pop() * count, result)
            count += 1
        return result
                    