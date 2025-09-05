# 很重要
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, k):
            # 终止条件1：越界或字符不匹配
            if not (0<= r < rows and 0 <= c < cols and board[r][c] == word[k]):
                return False
            
            # 终止条件2：成功找到单词的所有字符
            if k == len(word) - 1:
                return True

            # a. 做出选择：将当前格子标记为已访问，防止回头
            original_char = board[r][c]
            board[r][c] = '#'
            
            # b. 递归探索：向四个方向探索
            #    注意 k+1，因为我们要匹配下一个字符
            found = dfs(r + 1, c, k + 1) or \
                    dfs(r - 1, c, k + 1) or \
                    dfs(r, c + 1, k + 1) or \
                    dfs(r, c - 1, k + 1)
            
            # c. 撤销选择：恢复现场，以便其他路径可以使用这个格子
            board[r][c] = original_char

            return found
        
        # 主循环：尝试以每一个格子作为起点
        for r in range(rows):
            for c in range(cols):
                # 如果以 (r, c) 为起点，能找到单词，就返回 True
                if dfs(r, c, 0):
                    return True
        return False