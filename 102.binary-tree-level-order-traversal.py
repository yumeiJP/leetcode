#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if not root:
            return []

        res = []
        stack = collections.deque([root])
        
        while stack:
            n=len(stack)
            ls = []
            for _ in range(n):
                node = stack.popleft()

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                ls.append(node.val)
            
            res.append(ls)
        return res
        
        
        
# @lc code=end

