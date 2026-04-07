#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

"""
temperatures = [73,74,75,71,69,72,76,73]

i=0 --> check stack --> [0]

i=1 --> check stack [0]
73 < 74 --> keep stack, add to stack [0,1]

i=2-->check stack [0,1], 73 < 75 and 74 < 75 (this is where the redundancy is, 73<74 already checked)
[0,1,2]

i=3 -> check stack [0,1,2], 75 > 71 so add to output?
"""
        
# @lc code=end

