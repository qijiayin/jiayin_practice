#122 best-time-to-buy-and-sell-stock-ii/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(prices)-1, 0, -1 ):
            res += max(0, prices[i] - prices[i-1])


        return res
