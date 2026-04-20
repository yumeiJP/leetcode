#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def dfs(curr, open, close):
            if close > open or close > n or open > n:
                #invalid
                return
            
            if close == n and open == n:
                #valid
                res.append("".join(curr))
            
            if open < n:
                curr.append("(")
                dfs(curr, open+1, close)
                curr.pop()

            if open > close:
                curr.append(")")
                dfs(curr, open, close+1)
                curr.pop()
        
        dfs([], 0, 0)
        return res

        
# @lc code=end

