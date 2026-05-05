#
# @lc app=leetcode id=417 lang=python
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        ROWS = len(heights)
        COLS = len(heights[0])

        res = []

        info = [[set() for _ in range(COLS)] for _ in range(ROWS)]

        #() for unvisited
        #(0) for pacific only
        #(1) for atlantic only
        #(0,1) for both

        def dfs(r,c, prev_height):

            #pacific
            if r<0 or c<0:
                return set([0])
            #atlantic
            if r>= ROWS or c >= COLS:
                return set([1])
            
            #inbound confirmed
            
            height = heights[r][c]

            #return if cant flow in
            if prev_height < height:
                return set()

            #return if already explored
            if len(info[r][c]) > 0:
                return info[r][c]

            info[r][c] = info[r][c].union(dfs(r-1, c, height))
            info[r][c] = info[r][c].union(dfs(r+1,c, height))
            info[r][c] = info[r][c].union(dfs(r,c-1, height))
            info[r][c] = info[r][c].union(dfs(r,c+1, height))

            #if both explored, add to res
            if len(info[r][c]) == 2:
                res.append([r,c])

            return info[r][c]

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row,col, float('inf'))
        
        return res
        
# @lc code=end

