#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#

# @lc code=start

import heapq
import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        hashmap = {}
        heap = []
        queue = collections.deque([])

        if n == 0:
            return len(tasks)

        for num in tasks:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for key in hashmap.keys():
            freq = hashmap[key]
            heap.append(-freq)

        heapq.heapify(heap)

        time = 0

        while heap or queue:
            time += 1
            if heap:
                freq = heapq.heappop(heap)
                freq = freq+1

                if freq:
                    queue.append((freq,time+n))  

            if queue and queue[0][1] == time:
                #time to pop
                tuple = queue.popleft()
                heapq.heappush(heap, tuple[0])
        return time
        
# @lc code=end

