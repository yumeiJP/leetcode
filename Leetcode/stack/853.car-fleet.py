#
# @lc app=leetcode id=853 lang=python
#
# [853] Car Fleet
#

# @lc code=start

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        #output = len(position)
        n = len(position)

        l = []

        for i in range(n):
            p_val = position[i]
            s_val = speed[i]
            ls = (p_val, s_val)
            l.append(ls)

        l.sort(reverse = True)

        fleets = 0
        last_time = -1

        print(l)

        for i in range(n):
            print(i)
            x = l[i][0]
            v=l[i][1]

            #time = (target-x)//v

            time = (target-x)/v

            if time > last_time:
                fleets += 1
                last_time = time
        return fleets
        
# @lc code=end

