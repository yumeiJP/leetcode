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

        l1 = len(nums1)
        l2 = len(nums2)

        total = l1+l2
        half = int((l1+l2)/2)

        if l1 < l2:
            minnums = nums1
            maxnums = nums2
        else:
            minnums = nums2
            maxnums = nums1

        l = 0
        r = len(minnums)

        while True:
            m = int((l+r)/2)

            other_length = half-m

            if maxnums[other_length] > minnums[m+1]:
                #m too small
                l = m
            elif minnums[m+1] > maxnums[other_length]:
                #m too large
                r = m
            else: break
        
        n1 = l1[m+1]
        n2 = l2[m+1]
        if total%2 == 1:
            return min(n1, n2)
        elif total%2 == 0:
            return (n1+n2)/2



        
# @lc code=end

