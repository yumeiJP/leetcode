#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []

        dc = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        def dfs(i, curr, letter):
            nonlocal res
            if letter:
                curr.append(letter)
            if i==len(digits):
                string = "".join(curr)
                res.append(string)

                if letter: curr.pop()
                return
            

            for char in dc[int(digits[i])]:
                dfs(i+1, curr, char)
            if letter:
                curr.pop()
        
        dfs(0,[], "")
        return res
# @lc code=end

