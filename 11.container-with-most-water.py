#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        l=0
        r=n-1
        bestarea=0
        while l<r:
            shortest=min(height[l],height[r])
            diff=r-l
            area=shortest*diff
            bestarea=max(area,bestarea)

            h1=height[l]
            h2=height[r]
            if h1<=h2:
                l+=1
            elif h1>h2:
                r-=1
        return bestarea


        
# @lc code=end

