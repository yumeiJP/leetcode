#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        n = len(nums)
        triplets=[]

        for i in range(n):
            if i>0 and nums[i] == nums[i-1]: continue
            left = i+1
            right = n-1

            while left < right:

                sum = nums[i] + nums[left]+nums[right]

                if sum>0:
                    right -= 1
                elif sum<0:
                    left +=1
                else:
                    triplets.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right -=1
            
            

        return triplets
                        


        
# @lc code=end

