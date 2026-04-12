#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        best = 0

        def dfs(curr):
            left=0
            right=0

            if not curr:
                return 0

            if curr.left:
                left = dfs(curr.left)
            if curr.right:
                right = dfs(curr.right)
            
            nonlocal best
            best = max(left+right, best)

            return max(left,right)+1

        dfs(root)

        return best

        
# @lc code=end

