#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            
            else:
                if len(stack)==0:
                    return False
                stack_char = stack[-1]

                flipped_char = ""

                if char == ")":
                    flipped_char = "("
                elif char == "]":
                    flipped_char = "["
                elif char == "}":
                    flipped_char = "{"

                if flipped_char != stack_char:
                    return False
                
                stack.pop(-1)

        if len(stack) == 0:
            return True
        
        return False
            


"""
([]) case:

start with (, add it to stack
next for [, add it to stack
then for ], check if there is a [ on the -1 index, if there is, pop it
if there isnt, return false
"""
        
# @lc code=end

