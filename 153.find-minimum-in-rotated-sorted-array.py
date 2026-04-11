#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n=len(nums)
        l=0
        r=n-1

        if n == 1:
            return nums[0]
        
        while l<=r:
            m=(l+r)//2

            if nums[m]<nums[m-1]:
                return nums[m]

            if nums[m]>nums[0]:
                if l==r:
                    return nums[0]
                l=m+1
            elif nums[m]<nums[0]:
                r=m-1
            else:
                l = m+1
        return nums[l]
        
# @lc code=end

