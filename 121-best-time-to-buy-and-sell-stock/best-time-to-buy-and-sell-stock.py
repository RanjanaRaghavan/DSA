class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        max_profit = 0
        
        for p in prices:

            if p < buy:
                buy = p
            
            max_profit = max(max_profit, p-buy)
        
        return max_profit
        