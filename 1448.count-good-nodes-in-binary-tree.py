#
# @lc app=leetcode id=1448 lang=python
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 1
        def dfs(root, curr_max):
            nonlocal count

            if not root:
                return
            try:
                curr_max = max(curr_max,root.val)
            except:
                curr_max=0

            if root.left and root.left.val >= curr_max:
                count +=1
            if root.left:
                dfs(root.left, curr_max)
            if root.right and root.right.val >= curr_max:
                count +=1
            
            if root.right:
                dfs(root.right, curr_max)
        dfs(root, root.val)
        return count

        
        
# @lc code=end

