class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        string = str(x)
        length = len(string)

        palindrome = True

        for i in range(length):
            text1 = string[i]
            text2 = string[length-i-1]

            if text1 != text2:
                palindrome = False
        
        if palindrome:
            return True
        else:
            return False