#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        counts = []

        for string in strs:
            count = {}
            for char in string:
                count[char] = count.get(char, 0) + 1
            counts.append([string, count])
        
        for i in range(len(counts)):
            for j in range(i+1, len(counts)):
                #Check if anagram
                for c in counts[i]:
                    return
        
# @lc code=end

