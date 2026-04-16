#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        heap = []
        for num in stones:
            heap.append(-num)
        heapq.heapify(heap)

        while len(heap)>1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)

            if a!=b:
                heapq.heappush(heap, a-b)
        if len(heap)==0:
            return 0
        return -heap[0]

        
# @lc code=end

