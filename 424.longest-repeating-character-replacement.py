#
# @lc app=leetcode id=424 lang=python
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        l,r=0,0
        n=len(s)
        count=0
        best=0
        while r<n and l<=r:
            if s[r]!=s[l]:
                count+=1

            if count>k:
                if l+1>=n:
                    break
                if s[l+1]!=s[l]:
                    count-=1
                l+=1
                continue

            length = r-l+1
            best = max(best,length)
            print(l,r)
            print(count)
            print(best)
            r+=1

            
        return best

        
# @lc code=end

