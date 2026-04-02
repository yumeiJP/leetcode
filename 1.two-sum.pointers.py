#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        A = []

        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort()

        n = len(nums)

        l = 0
        r = n-1

        while l<r:
            sum = A[l][0] + A[r][0]

            if sum>target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [A[l][1], A[r][1]]

        
# @lc code=end

