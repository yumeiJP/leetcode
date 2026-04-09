#
# @lc app=leetcode id=875 lang=python
#
# [875] Koko Eating Bananas
#

# @lc code=start

import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        n = len(piles)
        l=0
        r=piles[-1]
        best = float('inf')

        while l<r:
            
        
        

        


        
# @lc code=end
"""
[4, 11, 20, 23, 30], h = 6

k=20 --> 12 hours --> 12 > 6

shes eating too slow --> k=23 --> 

if too fast, k = 11, if too slow, 23
binary search


"""