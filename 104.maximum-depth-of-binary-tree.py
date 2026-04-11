#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        if not (root.left or root.right):
            return 1
        
        left_depth = 0
        right_depth = 0

        if root.left:
            left_depth = self.maxDepth(root.left)
        if root.right:
            right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1


        
# @lc code=end

