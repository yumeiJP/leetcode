#
# @lc app=leetcode id=695 lang=python
#
# [695] Max Area of Island
#

# @lc code=start

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        width = len(grid[0])
        length = len(grid)
        visited = [[0]*width for _ in range(length)]
        stack = []
        max_area = 0
        
        for i in range(length):
            for j in range(width):
                if visited[i][j]==1 or grid[i][j] == 0: continue
                area = 0
                stack.append((i,j))
                while stack:
                    coord = stack.pop()
                    a,b=coord[0], coord[1]
                    if a<0 or b<0 or a>length-1 or b>width-1: continue
                    if visited[a][b]==1 or grid[a][b]==0: continue
                    area += 1
                    visited[a][b]=1
                    stack.append((a-1,b))
                    stack.append((a+1,b))
                    stack.append((a,b-1))
                    stack.append((a,b+1))
                max_area = max(area, max_area)
        
        return max_area
        
# @lc code=end

