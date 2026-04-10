#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n=len(nums)
        l=0
        r=n-1

        wall_index=0

        while l<r:
            m=(l+r-1)//2
            if nums[m]<nums[r]:
                r=m
            else:
                l=m+1
        wall_index=l

        print("a")

        l=0
        r=wall_index-1

        while l<=r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                return m
        
        l=wall_index
        r=n-1
        
        print("a")

        while l<=r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                return m

        return -1
        
# @lc code=end

