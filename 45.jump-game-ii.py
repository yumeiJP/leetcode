#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l,r=0,0
        res=0

        while r<len(nums)-1:
            furthest=0
            for i in range(l,r+1):
                furthest = max(furthest, nums[i]+i)
            l=r+1
            r=furthest
            res+=1
        return res


        
# @lc code=end

