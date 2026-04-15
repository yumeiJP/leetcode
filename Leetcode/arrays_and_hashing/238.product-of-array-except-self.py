#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)

        prefix = [1]*n
        suffix = [1]*n
        output = [1]*n

        prefix[0] = 1
        suffix[n-1] = 1

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1]*suffix[i+1]
        
        for i in range(n):
            output[i] = prefix[i] * suffix[i]
        
        return output


        
# @lc code=end

