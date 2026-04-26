#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        width = len(grid[0])
        length = len(grid)
        count = 0
        visited = [[0]*width for _ in range(length)]
        stack = []
        
        for i in range(length):
            for j in range(width):
                if visited[i][j]==1 or grid[i][j] == '0': continue
                stack.append((i,j))
                while stack:
                    coord = stack.pop()
                    a,b=coord[0], coord[1]
                    if a<0 or b<0 or a>length-1 or b>width-1: continue
                    if visited[a][b]==1 or grid[a][b]=='0': continue

                    visited[a][b]=1
                    stack.append((a-1,b))
                    stack.append((a+1,b))
                    stack.append((a,b-1))
                    stack.append((a,b+1))
                count += 1
        
        return count
        
# @lc code=end

