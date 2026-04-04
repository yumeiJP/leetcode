#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_height = 0
        for h in height:
            max_height = max(max_height,h)
        
        total = 0
        n=len(height)
        for k in range(max_height):
            l=0
            r=n-1

            while not height[l]>k:
                l+=1
            while not height[r]>k:
                r-=1 
                
            #Both has walls, now count the squares inbetween

            squares=1
            for i in range(l,r):
                if height[i]>k:
                    squares+=1
            
            total += r-l+1-squares
        return total
        
# @lc code=end

