# 很重要 PDD
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        # 栈中存放的是索引
        # 初始放入-1作为“边界”
        stack = [-1] 

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else: # char == ')'
                stack.pop()
                if not stack:
                    # 栈为空，说明当前的')'是一个无效的分割点
                    # 将它的索引放入，作为新的边界
                    stack.append(i)
                else:
                    # 栈不为空，计算有效长度
                    # i 是右边界，stack[-1] 是左边界
                    max_len = max(max_len, i - stack[-1])
        
        return max_len