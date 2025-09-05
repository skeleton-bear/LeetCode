class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # 从右上角开始搜索
        row = 0
        col = n - 1
        while row < m and col>=0 :
            current_val = matrix[row][col]

            if current_val == target:
                return True
            elif current_val > target:
                col -= 1
            else:
                row += 1
        return False
        