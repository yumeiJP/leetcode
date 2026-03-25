class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1,2]
        
        i = 3

        while i <= n:
            newStep = steps[i-2] + steps[i-3]
            steps.append(newStep)
            i+=1
        
        return steps[n-1]
