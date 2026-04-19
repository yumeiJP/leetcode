#
# @lc app=leetcode id=295 lang=python
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq
class MedianFinder(object):

    def __init__(self):
        self.left_heap_max=[]
        self.right_heap_min=[]
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        if not self.left_heap_max or num <= -self.left_heap_max[0]: #assuming equal can be ignored basically
            heapq.heappush(self.left_heap_max, -num)
        else:
            heapq.heappush(self.right_heap_min, num)
        
        #to check if tipping -> need to shift the left and rights
        left=len(self.left_heap_max)
        right=len(self.right_heap_min)

        if left>right+1:
            #tipping to left
            move = -heapq.heappop(self.left_heap_max)
            heapq.heappush(self.right_heap_min, move)
        elif right>left:
            #tipping to right
            move = heapq.heappop(self.right_heap_min)
            heapq.heappush(self.left_heap_max, -move) 

    def findMedian(self):
        """
        :rtype: float
        """
        left = len(self.left_heap_max)
        right = len(self.right_heap_min)
        if left>right:
            return -self.left_heap_max[0]
        else:
            return (-self.left_heap_max[0]+self.right_heap_min[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

