#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        l = 0
        r = n-1

        while l<r:
            m = (l+r)//2
            num = nums[m]

            if num == target:
                return m
            elif num > target:
                r = m-1
            else:
                l = m+1
        return l
        
# @lc code=end

