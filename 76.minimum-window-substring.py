#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        t_freq = [0]*26

        for letter in t:
            index = ord(letter)-ord("a")
            t_freq[index]+=1
        
        l,r=0,0

        n = len(s)

        prefix = []

        s_length = len(s)

        prefix.append([0]*26)

        first_letter = s[0]
        first_letter_index = ord(first_letter)-ord("a")

        prefix[0][first_letter_index] += 1

        for i in range(s_length):
            if i == 0: continue

            old_list = prefix[i-1]

            letter = s[i]

            letter_index = ord(letter)-ord("a")

            new_list = old_list[:]

            new_list[letter_index] += 1

            prefix.append(new_list)

        while r<n:
            window_freq = [0]*26
            if l>0:
                for i in range(26):
                    window_freq[i] = prefix[r][i]-prefix[l-1][i]
            if l==0:
                window_freq = prefix[r]
            
            contained = True

            for i in range(26):
                difference_in_freq = window_freq[i]-t_freq[i]
                if difference_in_freq<0:
                    contained = False
            
            if contained:
                l+=1
            else:
                r+=1
        
        output_string = ""

        for i in range(l, r+1):
            letter = s[i]
            output_string += letter
        return output_string



        
# @lc code=end

