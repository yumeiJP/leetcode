#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l,r=0,0
        best_length=0

        while r<len(s):
            hashset=set()
            repeating=False
            for i in range(l,r+1):
                letter=s[i]
                if letter in hashset:
                    repeating=True
                hashset.add(letter)
            
            if repeating:
                l+=1
                continue
            
            length = r-l+1
            best_length=max(length,best_length)
            print(l,r)
            r+=1
        return best_length
            
        
# @lc code=end

