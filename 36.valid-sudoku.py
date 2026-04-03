#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rowList = []
        columnList = []
        boxList = []

        for _ in range(9):
            rowList.append([0]*9)
            columnList.append([0]*9)
            boxList.append([[0]*9]*3)
        
        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number == ".": continue
                number = int(number)

                rowList[i][number-1] += 1
                columnList[j][number-1] += 1
                boxList[i//3][j//3][number-1] += 1
        
        print(rowList)
        print(columnList)
        print(boxList)

        for i in range(9):
            for j in range(9):
                n1 = rowList[i][j]
                n2 = columnList[i][j]

                if n1 > 1 or n2>1:
                    return False

                for k in range(9):
                    n3 = boxList[i][j][k]
                    if n3>1:
                        return False
        return True

        
# @lc code=end

