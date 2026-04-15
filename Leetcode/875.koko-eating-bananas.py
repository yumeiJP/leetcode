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

        piles.sort()
        n=len(piles)
        l=1
        r=piles[-1]
        best=float('inf')

        while l<=r:
            hours_needed=0
            m = (l+r)//2
            for i in range(n):
                if piles[i]>=m:
                    index=i
                    break
            hours_needed += index

            for i in range(index, n):
                ceil = math.ceil(piles[i]/m)
                hours_needed += ceil
            
            if hours_needed == h:
                best = min(best,m)
                r = m-1
            elif hours_needed > h:
                l = m+1
            else:
                best = min(best,m)
                r = m-1
        return best

"""
[3,6,7,11], h=8

l=3,r=11 --> m = 7
hours = 3+2=5
hours < h --> move r

l=3, r=6 -> m = 4
hours = 1 + (2+2+3)=8
guess=4

l=3,r=4 -> m=3
hours = 1+(2+3+3)=9


"""



        
        

        


        
# @lc code=end
"""
[4, 11, 20, 23, 30], h = 6

k=20 --> 12 hours --> 12 > 6

shes eating too slow --> k=23 --> 

if too fast, k = 11, if too slow, 23
binary search


"""