# 很重要
class Solution:
    def numSquares(self, n: int) -> int:
        # 1. 定义 dp 数组，dp[i] 表示和为 i 的最少完全平方数数量
        #    初始化 dp[0]=0, 其他为无穷大以便取 min
        dp = [math.inf] * (n + 1)
        
        # 3. 初始化边界条件
        dp[0] = 0
        
        # 4. 从前向后遍历
        for i in range(1, n + 1):
            # 内部循环遍历所有可能的平方数 j*j
            j = 1
            while j * j <= i:
                square = j * j
                # 2. 应用状态转移方程
                dp[i] = min(dp[i], dp[i - square] + 1)
                j += 1
                
        return dp[n]