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

        for task in tasks:
            hashmap[task] = hashmap.get(task, 0) + 1
        
        for key in hashmap.keys():
            val = hashmap[key]
            tuple = (-val, key)
            heap.append(tuple)
        
        heapq.heapify(heap)

        count = 0
        deque = collections.deque()

        while 1:
            print(heap, deque)
            if not heap and ((len(deque)==1 and deque[0] is int) or not deque):
                break

            k = len(deque)

            if deque:
                if deque[0] == 1:
                    deque.popleft()
                    if deque:
                        insert = deque.popleft()
                        heapq.heappush(heap, insert)
                else:
                    if deque[0] is int:
                        deque[0] = deque[0] - 1
            if not heap: 
                count += 1
                continue
            tuple = heapq.heappop(heap)
            print("spec", tuple, deque)
            if k==0:
                if n > 1:
                    deque.append(n-1)
                    deque.append((tuple[0]+1, tuple[1]))
            else:
                if -tuple[0] > 1:
                    deque.append((tuple[0]+1, tuple[1]))
            count += 1
        
        return count

        



        
# @lc code=end

