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

        max_lefts = []
        max_rights = []

        total=0

        n = len(height)
        
        max_left = 0
        max_right=0
        for i in range(n):
            max_left = max(max_left, height[i])
            max_lefts.append(max_left)
        for i in range(n-1, -1, -1):
            max_right = max(max_right, height[i])
            max_rights.append(max_right)
        max_rights.reverse()
        
        for i in range(n):
            max_left = max_lefts[i]
            max_right = max_rights[i]
            h=height[i]

            left = max(max_left-h,0)
            right=max(max_right-h,0)
            total+=min(left,right)
        
        return total
# @lc code=end

