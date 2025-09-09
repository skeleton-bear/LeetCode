class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] *n for _ in range(m)]

        # 初始化边界条件
        dp[0][0] = grid[0][0]

        # 初始化第一行和第一列
        for j in range (1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
         # 4. 从左到右、从上到下遍历
        for i in range(1, m):
            for j in range(1, n):
                # 2. 应用状态转移方程
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                
        return dp[m-1][n-1]
