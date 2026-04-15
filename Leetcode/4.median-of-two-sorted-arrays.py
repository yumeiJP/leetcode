#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        A,B = nums1,nums2
        total = len(nums1)+len(nums2)
        half=total//2
        if len(B)<len(A):
            A,B=B,A

        l=0
        r=len(A)-1

        while 1:
            i_a=(l+r)//2
            i_b=half-i_a - 2

            Aleft=A[i_a] if i_a>=0 else float('-inf')
            Aright=A[i_a+1] if i_a+1<len(A) else float('inf')
            Bleft=B[i_b] if i_b>=0 else float('-inf')
            Bright=B[i_b+1] if i_b+1<len(B) else float('inf')

            if Aleft <= Bright and Bleft < Aright:
                if total%2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                r=i_a-1
            else:
                l=i_a+1
            









        
# @lc code=end

