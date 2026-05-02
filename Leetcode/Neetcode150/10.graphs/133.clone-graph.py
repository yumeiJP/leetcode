# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        def dfs(node):
            if self.neighbors:
                for neighbor in self.neighbors:
                    curr = dfs(neighbor)
                    node.neighbors.append(curr)
            return node
            
        
