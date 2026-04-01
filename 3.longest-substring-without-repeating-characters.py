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

        string_length = len(s)
        best_list = []
        for length in range(string_length):
            current_list = []
            for index in range(string_length):
                #Check overflow
                if length + index >= string_length:
                    continue

                letter = s[length + index]

                #Check if repeating
                repeating = False
                for new_letter in current_list:
                    if letter == new_letter:
                        #Repeating
                        repeating = True
                
                if repeating:
                    break

                current_list.append(letter)
            
            if len(current_list) > len(best_list):
                best_list = current_list
        
        return len(best_list)




        

"""
- go through first index, first length
- for each index,
- make a list starting from first index and keep adding until the final length,
- checking if its repeating on the way
- if not repeating, save as best list and break
- if repeating, continue to next index
- if it was repeating on final index (check to not overflow), return answer 
"""

        
# @lc code=end

