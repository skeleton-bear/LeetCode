class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 转置矩阵然后水平反转
        # 转置矩阵,将上下三角区对换
        for r in range(n):
            for c in range(r+1,n):
                matrix[r][c], matrix[c][r] = matrix[c][r],matrix[r][c]
                
        # 水平反转
        for r in range(n):
            matrix[r].reverse()