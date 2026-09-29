class Solution:
    def maxProfit(self, p: List[int]) -> int:
        min_p = float('inf')
        max_profit = 0
        for price in p:
            min_p = min(min_p, price)
            max_profit = max(max_profit, price - min_p)
        return max_profit