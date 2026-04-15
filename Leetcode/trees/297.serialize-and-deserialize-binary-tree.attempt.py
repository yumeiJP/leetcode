#
# @lc app=leetcode id=297 lang=python
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root: return "|"

        order = []

        def preorder(root):
            nonlocal order
            order.append(str(root.val))
            order.append(",")
            if root.left: preorder(root.left)
            if root.right: preorder(root.right)
        preorder(root)
        order.append("|")

        def inorder(root):
            nonlocal order
            if root.left: inorder(root.left)
            order.append(str(root.val))
            order.append(",")
            if root.right: inorder(root.right)
        inorder(root)

        return "".join(order)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        pre=""
        ino=""
        pre = data.split("|")[0]
        ino = data.split("|")[1]

        pre_vals = [x for x in pre.split(",") if x]
        in_vals = [x for x in ino.split(",") if x]

        preorder = list(map(int,pre_vals))
        inorder = list(map(int, in_vals))

        pre_index=0

        in_map = {}
        for i in range(len(inorder)):
            in_map[inorder[i]] = i
        
        def dfs(l,r):
            if l>r: return None
            nonlocal pre_index
            mid=in_map[preorder[pre_index]]
            root=TreeNode(preorder[pre_index])
            pre_index+=1
            root.left=dfs(l,mid-1)
            root.right=dfs(mid+1,r)
            return root
        return dfs(0,len(inorder)-1)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

