# 很重要
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] *n

        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                # 弹出栈顶索引
                prev_index = stack.pop()
                # 计算天数差并记录
                answer[prev_index] = i - prev_index
            # 将当前索引压入栈中，等待未来找到更高温度
            stack.append(i)
        return answer


        