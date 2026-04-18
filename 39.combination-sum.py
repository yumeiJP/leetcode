#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        output = []

        def dfs(i, sum):
            if len(output)>150: return
            if sum > target: return
            if i >= len(candidates):
                if sum == target:
                    res.append(output.copy())
                return

            #print(output, sum)
            
            output.append(candidates[i])
            sum += candidates[i]

            dfs(i, sum)
            pop = output.pop()
            sum -= pop
            dfs(i+1,sum)
        
        dfs(0, 0)
        return res
        
# @lc code=end

