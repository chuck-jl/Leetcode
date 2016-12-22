class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit=0
        min_prices=prices[0]
        for i,k in enumerate(prices):
            max_profit=max(max_profit,k-min_prices)
            min_prices= min(min_prices,k)
        return max_profit