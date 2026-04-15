#
# @lc app=leetcode id=239 lang=python
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        n = len(nums)

        prefix_maximum = []

        output = []

        best = -float('inf')
        for i in range(n):
            num = nums[i]
            best = max(best, num)
            prefix_maximum.append(best)

        #Initial Step
        current_max = prefix_maximum[k-1]
        output.append(current_max)

        i=1

        while i+k-1<n:
            new_number = nums[i+k-1]
            leaving_number = nums[i-1]

            if leaving_number != current_max:
                i+=1
                output.append(current_max)
                continue

            #leaving number is current max
            if new_number>prefix_maximum[i+k-2]:
                current_max = new_number
            else:
                current_max = prefix_maximum[i+k-2]
            
            output.append(current_max)
            i+=1
    
        return output


        
# @lc code=end

"""
l=0 and r = k-1 at the beginning
you add 1 to both l and r every shift.

for first sliding window, the max is 3
now after shifting, you see the the new number is -3
you check if the leaving number, in this case, 1, was the maximum
if it was, then you have to check the max again... but thats not linear
if it wasnt, then you continue

track the maximum for each position?
like [1,3,3,3,5,5,6,7]

if the leaving number was the maximum, then you can check if ur current number
is higher than the prefix maximum?

you can also check if the new number is larger than the max then that new number
will definetelly be the max?
if it was smaller, then check if the new number is smaller than the prefix max 
for the previous position?
if it was smaller, then the previous position number should be the new max?
if it was larger, then the current position number should be the new max?

prefix_maximum: [1,3,3,3,5,5,6,7]
0. [1 3 -1] -3 5 3 6 7 -> initial step, current_max = 3
1. 1 [3 -1 -3] 5 3 6 7 -> levaing number is 1, and it isnt current_max so continue
2. 1 3 [-1 -3 5] 3 6 7 -> leaving number is 3, and it is current_max. is 5 greater
than the prefix_maximum before it? prefix_maximum[3] == 3 where 5>3 so new number
should be new current_max = 5
3. 1 3 -1 [-3 5 3] 6 7 -> leaving number = -1 < 5
4. 1 3 -1 -3 [5 3 6] 7 -> leaving number = -3 < 5
5. 1 3 -1 -3 5 [3 6 7] -> leaving number = 5 = current_max -> new number is 7.
is new number > prefix_maximum[6]=6? yes. so current_max = new_number = 7

probably works
"""