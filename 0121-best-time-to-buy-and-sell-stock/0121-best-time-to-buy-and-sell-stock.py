class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        sell = 1
        maxProfit = 0
        while sell < len(prices):
            if prices[buy] >= prices[sell]:
                buy = sell
            else:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
            sell += 1
        return maxProfit
        