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

        hashmap = {}
        for coord in points:
            val = coord[0]**2 + coord[1]**2
            if hashmap.get(val, "skibidi")=="skibidi":
                hashmap[val] = []
            hashmap[val].append(coord)

        heap = []
        heapq.heapify(heap)
        for i in range(k):
            coord = points[i]
            val = coord[0]**2 + coord[1]**2
            heapq.heappush(heap, -val)
        
        for i in range(k, len(points)):
            
            coord = points[i]
            val = coord[0]**2 + coord[1]**2
            if val < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -val)
        output = []

        while len(output)<k:
            num = heapq.heappop(heap)
            ls = hashmap[-num]
            output.append(ls.pop())
        
        return output
        
# @lc code=end

