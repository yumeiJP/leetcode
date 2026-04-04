#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        lowest_searched=9999999
        best_profit=0

        for i in range(n):
            if prices[i]>lowest_searched:
                continue
            for j in range(i+1,n):
                new_price = prices[j]
                diff = new_price - prices[i]
                best_profit = max(best_profit, diff)
            lowest_searched=min(lowest_searched, prices[i])
        return best_profit
                
        
# @lc code=end

