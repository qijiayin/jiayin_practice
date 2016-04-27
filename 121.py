# 121 best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1 : return 0
        maxProf = 0
        minPrice = prices[0]
        for i in range(1, len(prices) ):
            minPrice = min(minPrice, prices[i])
            maxProf = max(maxProf, prices[i] - minPrice )

        return maxProf
