#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """
        min-heap with fixed length k

        keep pushing if the length is less than k
        if length is at least k,
        check whether root of min-heap (the minimum) is larger or less than the new number
        if larger, replace
        if smaller, skip

        at the end, pop k times.

        edge cases:
        nums = [2]
        at heap [], it will push [2] and end and push and send 2.
        """
        heap = []

        for num in nums:
            if len(heap)<k:
                heapq.heappush(heap, num)
                continue
            if heap[0]>num:
                continue
            heapq.heapreplace(heap, num)

        return heap[0]
            

# @lc code=end

