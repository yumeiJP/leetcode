#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length = len(nums)
        triplets = []
        
        nums.sort()

        for i in range(length-2):
            l=i+1
            r = length-1

            sum = nums[l]+nums[r]
            
            

        return triplets
                        


        
# @lc code=end

