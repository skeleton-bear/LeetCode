# 很重要 字节
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # # 添加哨兵,保证清空栈
        heights.append(0)
        n = len(heights)

        stack = [-1]
        max_area = 0

        for i in range(n):
            # 维持一个单调递增栈
            # 如果当前柱子高度小于栈顶，说明栈顶柱子的右边界找到了
            while heights[i] < heights[stack[-1]]:
                # 弹出栈顶，计算以此为高的矩形面积 
                h = heights[stack.pop()]

                #左边界是弹出后，新的栈顶
                left_boundary = stack[-1]

                # 宽度 = 右边界 i - 左边界 - 1
                width = i - left_boundary - 1

                max_area = max(max_area, h * width)

            # 当前柱子索引入栈
            stack.append(i)
        return max_area

        