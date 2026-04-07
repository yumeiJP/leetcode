#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        n = len(temperatures)

        stack = []
        output = [0]*n

        for i in range(n):
            if len(stack) == 0:
                stack.append(i)
                continue

            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                output[index] = i-index
            
            stack.append(i)
        
        return output



"""
[73 74 75 71 69 72 76 73]

i=0-> 73 -> stack empty so append to stack [0]
i=1-> 74 -> 73 (top of stack) < 74 (temp) so pop top stack output[0]=1 append to stack [1]
i=2-> 75 -> 74<75 so pop top stack output[0]=1 append to stack [2]
i=3-> 71 -> 75>71 so append to stack [2, 3]
i=4-> 69 -> stack[-1]=71>69 so append to stack [2, 3,4]
i=5-> 72 -> 69<72 so output[4] = 1 pop top stack [2, 3] 71 < 72 so utput[3] = 2 pop top stack [2] and so on
"""
        
# @lc code=end

