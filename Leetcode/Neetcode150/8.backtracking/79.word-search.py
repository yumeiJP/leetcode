#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        width = len(board[0])
        length = len(board)

        visited = [[0]*width for _ in range(length)]

        def dfs(i,j,k):
            nonlocal visited
            if i < 0 or j < 0 or i >= length or j >= width or visited[i][j] == 1 or board[i][j]!=word[k]:
                #invalid
                return False
            
            if k == len(word)-1:
                #valid
                return True
            
            visited[i][j] = 1
            found = dfs(i+1, j, k+1) or dfs(i,j+1,k+1) or dfs(i-1,j,k+1) or dfs(i,j-1,k+1)
            visited[i][j] = 0
            return found
        
        for i in range(length):
            for j in range(width):
                if dfs(i,j,0):
                    return True
        return False
        
# @lc code=end

