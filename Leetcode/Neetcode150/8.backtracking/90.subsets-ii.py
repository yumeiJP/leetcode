#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def dfs(i, curr):
            res.append(curr.copy())

            for j in range(i, len(nums)):
                if j > i and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[j])
                dfs(j+1, curr)
                curr.pop()
        
        dfs(0, [])
        return res
        
# @lc code=end

