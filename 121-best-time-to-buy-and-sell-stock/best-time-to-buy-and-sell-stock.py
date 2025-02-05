class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        maxprofit = 0

        for p in prices:

            if p < buy:
                buy = p
            
            profit = p - buy
            maxprofit = max(maxprofit,profit)
        
        return maxprofit
            


        