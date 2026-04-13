#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        balanced = True

        if not root:
            return True

        def dfs(curr):
            if not curr:
                return 0
            
            left=0
            right=0

            if curr.left:
                left=dfs(curr.left)
            if curr.right:
                right=dfs(curr.right)

            nonlocal balanced
            
            if left!=right+1 and right!=left+1 and left!=right:
                balanced = False
            
            return max(left,right)+1

        dfs(root)

        if balanced:
            return True
        else:
            return False
        
# @lc code=end

