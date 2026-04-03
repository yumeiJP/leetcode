#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]


        [1,1,1,1,2,2,2,3,3,5,5,5,5,5]
        1 --> 4
        2 --> 3
        3 --> 2
        5 --> 5
        sort based on hashmap
        """

        count = {}

        n = len(nums)

        for i in range(n):
            num = nums[i]

            count[num] = count.get(num, 0) + 1
        
        countL = []
        #freq, num

        for key in count.keys():
            frequency = count[key]
            countL.append([frequency, key])

        countL.sort()
        countL.reverse()

        output = []

        for i in range(k):
            output.append(countL[i][1])
        return output





        
# @lc code=end

