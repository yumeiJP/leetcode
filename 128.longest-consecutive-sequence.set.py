#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_set = set(nums)
        best_length = 0

        for num in nums_set:
            if num -1 in nums_set: continue

            length = 1
            current = num
            
            while current + 1 in nums_set:
                current +=1
                length+=1

            best_length = max(length, best_length)
        return best_length
            




        
# @lc code=end

