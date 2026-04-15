#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        p = ""

        for char in s:
            if char == " ":
                continue
            if not(char.isalpha() or char.isdigit()):
                continue

            p += char.lower()
        length = len(p)

        i=0
        palindrome = True

        while i < length/2:
            if not(p[i] == p[-i-1]):
                palindrome = False
            i += 1
        
        return palindrome
        
# @lc code=end

