#
# @lc app=leetcode id=235 lang=python
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root.val==p.val or root.val==q.val:
            return root

        def contains(node,p,q):
            if not node:
                return False
            if node.val==p.val or node.val==q.val:
                return True
            if node.left and contains(node.left,p,q):
                return True
            if node.right and contains(node.right,p,q):
                return True
            return False
        
        left,right=0,0
        if root.left and contains(root.left,p,q):
            left=1
        if root.right and contains(root.right,p,q):
            right=1
        if left==right:
            return root
        elif left==1:
            return self.lowestCommonAncestor(root.left,p,q)
        elif right==1:
            return self.lowestCommonAncestor(root.right,p,q)

        
# @lc code=end

