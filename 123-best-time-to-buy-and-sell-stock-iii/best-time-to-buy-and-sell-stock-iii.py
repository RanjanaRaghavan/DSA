class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        t1Buy, t2Buy = float("inf"), float("inf")
        t1Profit, t2Profit = 0,0

        for price in prices:

            t1Buy = min(t1Buy, price)
            t1Profit = max(t1Profit, price - t1Buy)

            t2Buy = min(t2Buy, price - t1Profit)
            t2Profit = max(t2Profit, price - t2Buy)

        return t2Profit
        