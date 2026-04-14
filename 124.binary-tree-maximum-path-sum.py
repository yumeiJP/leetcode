#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        best=float('-inf')

        def dfs(root):
            nonlocal best
            if not root: return 0
            
            left,right=0,0
            if root.left: left = dfs(root.left)
            if root.right: right = dfs(root.right)
            sum1 = left+right+root.val
            sum2 = left+root.val
            sum3 = right+root.val
            sum4=root.val

            best = max(best, sum1, sum2, sum3, sum4)

            return max(sum2, sum3, sum4)
        dfs(root)
        return best
        
# @lc code=end

