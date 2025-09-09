class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # dp[i] 的定义：凑成总金额为 i 所需的最少硬币个数。
        # dp[i] = min(dp[i-coin] + 1)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
        
        