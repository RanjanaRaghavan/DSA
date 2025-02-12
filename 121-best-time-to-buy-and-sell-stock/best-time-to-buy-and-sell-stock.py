class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        maxprofit = 0

        for p in prices:

            if p < buy:
                buy = p
            
            maxprofit = max(maxprofit, p - buy)

        return maxprofit
        