#
# @lc app=leetcode id=572 lang=python
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(curr1, curr2):

            if not curr1 and not curr2:
                return True
            if not curr1 and curr2:
                return False
            if curr1 and not curr2:
                return False
            
            if curr1.val != curr2.val:
                return False

            return dfs(curr1.left, curr2.left) and dfs(curr1.right, curr2.right)
        
        return dfs(p,q)

    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """

        if self.isSameTree(root, subRoot):
            return True

        if root.left:
            if self.isSubtree(root.left, subRoot):
                return True
        if root.right:
            if self.isSubtree(root.right, subRoot):
                return True

        return False

        
# @lc code=end

