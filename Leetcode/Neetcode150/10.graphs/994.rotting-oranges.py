#
# @lc app=leetcode id=994 lang=python
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        from collections import deque

        q = deque([])
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]
        total = 0
        tracked = 0
        time = -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                    tracked += 1
                if grid[i][j] != 0:
                    total += 1
        
        def infect(i,j):
            nonlocal tracked
            if not (0<=i<len(grid) and 0<=j<len(grid[0])): return
            if grid[i][j] == 0 or grid[i][j] == 2: return
            if visited[i][j]: return

            visited[i][j] = 1
            tracked += 1
            q.append((i,j))

        while q:
            time += 1
            for _ in range(len(q)):
                #print(q, time, tracked)
                coord = q.popleft()
                i = coord[0]
                j = coord[1]

                infect(i+1,j)
                infect(i-1,j)
                infect(i,j+1)
                infect(i,j-1)
            
        
        #print(time, total, tracked)
        if total == tracked:
            if time == -1:
                return 0
            return time
        else:
            return -1



        
# @lc code=end

