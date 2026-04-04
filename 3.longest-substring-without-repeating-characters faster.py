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
        hashset=set()

        while r<len(s):
            letter = s[r]
            
            if letter in hashset:
                hashset.remove(s[l])
                l+=1
                continue

            hashset.add(letter)
            
            length = r-l+1
            best_length=max(length,best_length)
            print(l,r)
            r+=1
        return best_length
            
        
# @lc code=end

