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
            temp = temperatures[i]

            
            if len(stack) == 0 or temperatures[stack[-1]] >= temp:
                stack.append(i)
                continue

            while len(stack)>0 and temperatures[stack[-1]] < temp:
                    
                index = stack[-1]

                output[index] = i-index
                stack.pop()

                print(i, index, temp)
                print("output", output)
                print("stack:", stack)
        
        return output

"""
temperatures = [73,74,75,71,69,72,76,73]

i=0 --> check stack --> [0]

i=1 --> check stack [0]
73 < 74 --> keep stack, add to stack [0,1]

i=2-->check stack [0,1], 73 < 75 and 74 < 75 (this is where the redundancy is, 73<74 already checked)
[0,1,2]

i=3 -> check stack [0,1,2], 75 > 71 so add to output?
output[2] = i-2 = 1
pop from stack --> [0,1]

74 > 71 so add to output
output[1] = i-1 = 2
pop from stack --> [0]

73 > 71 so add to output
output[0] = i-0 = 3
pop from stack --> []

repeat until empty (while loop)
"""
        
# @lc code=end

