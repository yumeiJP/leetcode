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
        print("serialize called with root:", root)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []

        if not root: return "null"
        
        def dfs(root):
            nonlocal data
            data.append(str(root.val))
            if root.left: dfs(root.left)
            else: data.append("N")
            if root.right: dfs(root.right)
            else: data.append("N")

        return ",".join(data)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        i=0

        if data == "null":
            return None

        datals = data.split(",")

        def dfs():
            nonlocal i 
            nonlocal datals
            
            val = datals[i]
            i+=1
            
            if val == "N" or val == "":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            
            

            return node
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

