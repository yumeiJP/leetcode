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
        best_profit =0

        min_buy=999999

        for price in prices:
            profit=price-min_buy
            min_buy=min(price, min_buy)
            best_profit=max(best_profit,profit)
        return best_profit
                
        
# @lc code=end

