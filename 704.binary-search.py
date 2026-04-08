#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        l=0
        r=n-1

        while l<=r:
            m = (l+r)//2
            num = nums[m]

            if num == target:
                return m
            elif num > target:
                r = m-1
            elif num < target:
                l = m+1
        return -1
            
        
# @lc code=end

