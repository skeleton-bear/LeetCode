class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m,n = len(matrix), len(matrix[0])

        # 当作一个一维数组来找
        left, right = 0, m*n - 1

        while left <= right:
            mid = (left+right) // 2

            row = mid //n
            col = mid % n

            mid_val = matrix[row][col]

            if mid_val == target:
                return True

            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False # 没找到
        