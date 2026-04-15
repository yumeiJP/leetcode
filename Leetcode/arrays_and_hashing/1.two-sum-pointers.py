class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            number = nums[i]

            search = target - number

            for j in range(len(nums)):

                if i==j:
                    continue
                
                if search == nums[j]:
                    return [i,j]