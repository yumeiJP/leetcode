#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(map(str, s))
        t = list(map(str, t))

        s.sort()
        t.sort()

        if s==t:
            return True
        return False
        
# @lc code=end

