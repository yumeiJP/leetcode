#
# @lc app=leetcode id=567 lang=python
#
# [567] Permutation in String
#

# @lc code=start
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1)>len(s2):
            return False

        s1_freq = [0]*26

        for letter in s1:
            index = ord(letter)-ord("a")
            s1_freq[index] += 1
        
        n = len(s1)
        N = len(s2)
        freq_list = []
        initial_list = [0]*26
        
        l = 0
        r = l+n-1

        for i in range(l, r+1, 1):
            letter = s2[i]
            index = ord(letter)-ord("a")

            initial_list[index] += 1
        
        freq_list.append(initial_list)

        for i in range(n, N):
            old_list = freq_list[i-n]
            new_list = old_list[:]

            letter1=s2[i-n]
            letter2=s2[i]

            letter1_index=ord(letter1)-ord("a")
            letter2_index=ord(letter2)-ord("a")

            new_list[letter2_index] += 1
            new_list[letter1_index] -= 1

            freq_list.append(new_list[:])
        
        for freq in freq_list:
            if freq == s1_freq:
                return True
        return False
        


        
# @lc code=end

