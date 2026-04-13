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

        valid = True

        def dfs(curr1, curr2):
            nonlocal valid
            left1, left2,right1,right2=0,0,0,0

            if not curr1 and not curr2:
                return
            if not curr1 and curr2:
                valid = False
                return
            if curr1 and not curr2:
                valid = False
                return

            if curr1.left: left1 = 1
            if curr1.right: right1=1
            if curr2.left:left2=1
            if curr2.right:right2=1

            print(left1, left2, right1, right2)

            if (left1!=left2)or(right1!=right2):
                valid = False
                return
            
            if curr1.val != curr2.val:
                valid = False
                return
            
            if curr1.left and curr2.left:
                dfs(curr1.left, curr2.left)
            if curr1.right and curr2.right:
                dfs(curr1.right, curr2.right)
        
        dfs(p,q)
            
        return valid

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

