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
            #boxList.append([[0]*9]*3)

        boxList = [[[0]*9 for _ in range(3)] for _ in range(3)]

        print(boxList[0][0])

        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number == ".": continue
                number = int(number)

                rowList[i][number-1] += 1
                columnList[j][number-1] += 1
                print(i, j, number-1)
                boxList[i//3][j//3][number-1] += 1

                if rowList[i][number-1]>1 or columnList[j][number-1]>1 or boxList[i//3][j//3][number-1]>1:
                    return False
        print(rowList)
        print(columnList)
        print(boxList)
        
        return True
        


        
# @lc code=end

