class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 找到最大和最小的价差,其中大价格的下标需要在小价格前面
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, (price - min_price))
            min_price = min(min_price,price) # 这样保证price永远在min_price前面
        return max_profit

        