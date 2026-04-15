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
        best_profit =0

        min_costs = []
        min_cost=999999


        for i in range(n):
            price = prices[i]
            min_cost=min(price,min_cost)
            min_costs.append(min_cost)
        
        for i in range(n):
            price = prices[i]
            profit = price-min_costs[i]
            best_profit = max(profit,best_profit)
        
        return best_profit
                
        
# @lc code=end

