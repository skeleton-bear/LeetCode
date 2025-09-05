class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        row, col = len(grid), len(grid[0])
        island_count = 0

        for r in range(row):
            for c in range(col):

                if grid[r][c] == '1':
                    island_count += 1
                    # 使用DFS将他连通的点全部置0
                    self.dfs(grid, r,c)
        return island_count

    def dfs(self, grid, r, c):
        row, col = len(grid), len(grid[0])

        # 终止条件 / 边界检查
        if not (0 <= r < row and 0 <= c < col and grid[r][c] == '1'):
            return
        # 将当前格子置0
        grid[r][c] = '0'

        # 向四个方向递归扩散
        self.dfs(grid, r + 1, c) # 下
        self.dfs(grid, r - 1, c) # 上
        self.dfs(grid, r, c + 1) # 右
        self.dfs(grid, r, c - 1) # 左
            