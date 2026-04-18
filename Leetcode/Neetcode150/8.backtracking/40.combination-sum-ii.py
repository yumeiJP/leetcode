#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        candidates.sort()

        def dfs(i, curr, sum):
            if target == sum:
                res.append(curr.copy())
                return
            if i >= len(candidates) or sum > target: return

            curr.append(candidates[i])

            dfs(i+1, curr, sum + candidates[i])
            curr.pop()

            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            
            dfs(i+1, curr, sum)
        
        dfs(0, [], 0)
        return res


        
# @lc code=end

