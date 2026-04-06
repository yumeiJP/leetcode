#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        T = {}
        W = {}
        have = 0

        best_length = float("infinity")
        best_index = [0,0]

        for letter in t:
            T[letter] = T.get(letter,0) + 1
        
        need = len(T)
        
        l,r = 0,0

        for r in range(len(s)):
            letter = s[r]

            if T.get(letter)>=1:
                W[letter] = W.get(letter,0) + 1
            
            if letter in T and W[letter]==T[letter]:
                have +=1
            
            while have >= need:
                length = r-l+1

                if length < best_length:
                    best_length = length
                    best_index = [l,r]
                
                letterL = s[l]
                if letterL in T:
                    if W[letterL]==T[letterL]:
                        have -=1
                    W[letterL]-=1
                l+=1
        
        output = ""
        if best_length == float("inf"):
            return ""
        for i in range(best_index[0], best_index[1]+1):
            letter = s[i]
            output += letter
        return output
            
        



        
# @lc code=end

