#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        for t in tokens:
            if t in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(t))
        return stack[0]

        
# @lc code=end

"""
tokens = ["4","13","5","/","+"]

r = 0

start by looking at index 2 and seeing if its one of the operators
if it isnt, just keep moving till you see an operator

do the opreation using the operator and the two numbers before it,
get the result, replace the operator with the result, and pop the other 2 index

repeat until the token just becomes length 1 number array and output that
"""

