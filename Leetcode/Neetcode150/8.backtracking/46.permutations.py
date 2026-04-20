#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(output, included):
            if len(output)==len(nums):
                #valid
                res.append(output.copy())
                return
            for num in nums:
                if num in included:
                    #invalid
                    continue
                
                output.append(num)
                included.add(num)

                dfs(output, included)
                output.pop()
                included.remove(num)
        
        dfs([], set())
        return res

        
# @lc code=end

