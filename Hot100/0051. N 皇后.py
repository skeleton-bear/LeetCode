# 很重要
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        path = [-1] * n # 每行皇后放置的列号

        cols_used = set()
        diag1_used = set()
        diag2_used = set()

        self.backtrack(n, 0, path, result, cols_used, diag1_used, diag2_used)

        return result

    def backtrack(self, n, row, path, result, cols_used, diag1_used, diag2_used):
        if row == n:
            # 将 path 转换成题目要求的棋盘格式
            board = self._generate_board(n, path)
            result.append(board)
            return

        for col in range(n):
            if col in cols_used or (row - col) in diag1_used or (row + col) in diag2_used:
                continue

            # --- 回溯三部曲 ---
            # 1. 做出选择
            path[row] = col
            cols_used.add(col)
            diag1_used.add(row - col)
            diag2_used.add(row + col)

            # 2. 递归进入下一行
            self.backtrack(n, row + 1, path, result, cols_used, diag1_used, diag2_used)

            # 3. 撤销选择 (恢复现场)
            # path[row] 会在下一次循环中被覆盖，无需显式撤销
            cols_used.remove(col)
            diag1_used.remove(row - col)
            diag2_used.remove(row + col)

    def _generate_board(self, n, path):
        board = []
        for col_index in path:
            row_string = "." * col_index + "Q" + "." * (n - col_index - 1)
            board.append(row_string)
        return board
             
        
        