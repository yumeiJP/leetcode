#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        max_reachable = 0

        n = len(nums)

        for i in range(n):
            num = nums[i]

            if i>max_reachable:
                return False
            
            max_reachable = max(max_reachable, i+num)

            if i+num>=n-1:
                return True
        
# @lc code=end

