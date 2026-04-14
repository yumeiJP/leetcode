#
# @lc app=leetcode id=105 lang=python
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        inorder_map = {}

        for i in range(len(inorder)):
            val = inorder[i]
            inorder_map[val]=i

        self.pre_index=0

        def dfs(l,r):
            if l>r:
                return None
            
            mid = inorder_map[preorder[self.pre_index]]
            root = TreeNode(preorder[self.pre_index])
            self.pre_index += 1

            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        
        return dfs(0, len(inorder)-1)

        
# @lc code=end

