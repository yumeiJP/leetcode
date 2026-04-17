#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        heap = []
        heapq.heapify(heap)
        for i in range(k):
            coord = points[i]
            val = coord[0]**2 + coord[1]**2
            heapq.heappush(heap, (-val, coord))
        
        for i in range(k, len(points)):
            coord = points[i]
            val = coord[0]**2 + coord[1]**2
            if val < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-val, coord))
        output = []

        while len(output)<k:
            tuple = heapq.heappop(heap)
            output.append(tuple[1])
        
        return output
        
# @lc code=end

