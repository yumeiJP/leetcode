class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n = len(nums)

        nums.sort()

        for i in range(n):
            if nums[i] == nums[i-1] and i>=1:
                return True
        return False