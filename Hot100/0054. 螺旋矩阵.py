class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        left, right, top, bottom = 0, (n-1), 0, (m-1)
        result = []
        # 循环指导所有元素都被访问
        while left<= right and top <= bottom:
            for col in range(left, right+1):
                result.append(matrix[top][col])
            top += 1

            for row in range(top, bottom+1):
                result.append(matrix[row][right])
            right -=1

            # 检查是否还有有效行列
            if top <= bottom:
                # 3. 从右到左遍历下边界
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1 # 下边界上移

            if left <= right:
                # 4. 从下到上遍历左边界
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1 # 左边界右移
        return result
        