#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashmap = {}

        for num in nums:
            for i in range(-1,2):
                list = hashmap.get(num+i)
                value = 0
                if i ==0:
                    value = 1
                
                if list is None:

                    list = [[],value]
                
                if list[1] == 1:
                    value = 1
                
                innerlist = list[0]
                if num not in innerlist:
                    innerlist.append(num)
                
                list[0] = innerlist
                list[1] = value
                
                hashmap[num+i] = list

            print(hashmap)
            
        
        
        best = 0
        for key in hashmap.keys():
            speciallist = hashmap[key]
            if speciallist[1] != 1:
                continue

            length = len(speciallist[0])

            if length > best:
                best = length
        
        return best


        
# @lc code=end

