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
        height = len(board)
        visited = [[[0]*width]*height]
        valid = False

        def dfs(i,j,k):
            nonlocal valid
            if valid: return

            if k == len(word-1):
                valid = True
                return

            if i+1<height and board[i+1][j] == word[k] and visited[i+1][j]==0:
                visited[i+1][j]==1
                dfs(i+1,j,k)
                visited[i+1][j]==0
            if i-1>0 and board[i-1][j]
        
# @lc code=end

