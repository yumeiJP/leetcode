#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        new_strs = []
        output = []

        for string in strs:
            new_strs.append(tuple(sorted(string)))
        
        hashmap = {}

        for i in range(len(new_strs)):
            string = new_strs[i]

            if string not in hashmap:
                hashmap[string] = [i]
            else:
                hashmap[string].append(i)
        
        for key in hashmap.keys():

            indexes = hashmap[key]
            skibidi = []
            for index in indexes:
                skibidi.append(strs[index])
            output.append(skibidi)
        return output



            

        

        
        
# @lc code=end

