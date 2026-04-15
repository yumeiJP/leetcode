class Solution:
    def mySqrt(self, x: int) -> int:
        string = str(x)
        #numberOfDigits = len(string)

        index = 0
        while index**2 <= x:
            index += 1
        
        return int(index-1)
