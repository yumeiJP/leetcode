#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current = -float('inf')

        best = -float('inf')

        r=0

        for r in range(len(nums)):
            num = nums[r]
            
            current = current + num

            if current < num:
                current = num
            best = max(best, current)
        
        return best




        
# @lc code=end

