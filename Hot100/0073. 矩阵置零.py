class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先标记然后再赋值,使用第一行和第一列来存储标记

        m, n = len(matrix), len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False
        
        for c in range(n):
            if matrix[0][c] == 0:
                first_row_has_zero  = True
                break
        
        for r in range(m):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
        
        # 遍历矩阵,使用第一行/列来记录是否需要置0
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # 各方那句第一行列的标记来处理置0
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # 处理第一行和列
        if first_row_has_zero:
            for c in range(n):
                matrix[0][c] = 0
        if first_col_has_zero:
            for r in range(m):
                matrix[r][0] = 0

        