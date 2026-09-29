class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best_profit = 0
        for i in range(1,len(prices)):
            price = prices[i]
            lowest = min(price,lowest)
            best_profit = max(price - lowest, best_profit)

        return best_profit

        