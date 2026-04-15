#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        valid = True
        def dfs(root, lower, upper):
            nonlocal valid

            if not valid:
                return

            if not root:
                return

            if root.left and not (root.left.val > lower and root.left.val < min(root.val, upper)):
                valid = False
            if root.right and not (root.right.val > max(root.val ,lower) and root.right.val < upper):
                valid = False
            
            if root.left:
                dfs(root.left, lower, min(root.val, upper))
            if root.right:
                dfs(root.right, max(root.val, lower), upper)
        
        dfs(root,float('-inf'),float('inf'))
        return valid
        
        
# @lc code=end

