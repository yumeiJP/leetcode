#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        res = []

        def dfs(i, curr_str_list, curr):
            nonlocal res
            #valid
            if i == len(s):
                res.append(curr.copy())

            #initialize
            curr_str_list.append(s[i])

            #join
            dfs(i+1, curr_str_list, curr)
            curr.pop()
            curr_str_list.pop()
            
            #split
            
            #check if palindrome
            n=len(curr_str_list)
            for j in range(n//2):
                if curr_str_list[j] != curr_str_list[n-j-1]:
                    return
            curr.append("".join(curr_str_list))
            dfs(i+1, curr_str_list, curr)
            curr.pop()
        dfs(0, [], [])

        return res
            
        
# @lc code=end

