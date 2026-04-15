#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """


        def counterManage(root):
            count = 0
            def counter(root):
                nonlocal count
                if not root:
                    return

                count += 1

                if root.left: counter(root.left)
                if root.right: counter(root.right)
            counter(root)
            return count

        count = counterManage(root.left)

        if k<count+1:
            return self.kthSmallest(root.left, k)
        elif k==count+1:
            return root.val
        else:
            return self.kthSmallest(root.right, k-count-1)
        
# @lc code=end

