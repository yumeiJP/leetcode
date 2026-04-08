#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        correct_row = 0

        n = len(matrix)

        l = 0
        r = n-1

        while l<=r:
            m = (l+r)//2
            num = matrix[m][0]

            if num == target:
                return True
            elif num < target:
                l = m+1
            elif num > target:
                r = m-1
        
        correct_row = l-1
        print(correct_row)

        l=0
        r = len(matrix[0])-1

        while l<=r:
            m=(l+r)//2
            num=matrix[correct_row][m]

            if num == target:
                return True
            elif num < target:
                l = m+1
            elif num > target:
                r = m-1
        
        return False

        
# @lc code=end

