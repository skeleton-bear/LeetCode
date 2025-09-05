from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_orange_count = 0

        # 1. 初始化：将所有腐烂橘子入队，并统计新鲜橘子数量
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_orange_count += 1
                elif grid[r][c] == 2:
                    queue.append((r, c)) # 等会要上下左右都腐烂
        
        if fresh_orange_count == 0:
            return 0
        
        minutes = 0
        # 定义四个方向
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 多源BFS
        while queue and fresh_orange_count > 0:
            # 每一轮while就是一分钟
            level_size = len(queue)
            minutes += 1
            
            for _ in range(level_size):
                r, c = queue.popleft()

                # 向四个方向扩散
                for dr, dc in directions:
                    nr, nc = r + dr,  c + dc

                    # 检查另据是否合法且新鲜
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # 腐烂
                        grid[nr][nc] = 2
                        # 加入队列成为传染源
                        queue.append((nr, nc))
                        # 新鲜橘子减少1
                        fresh_orange_count -= 1
        
        return minutes if fresh_orange_count == 0 else -1


        