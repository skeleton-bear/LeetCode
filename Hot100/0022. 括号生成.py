class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        self.backtrack(n, path, 0, 0, result)
        return result

    def backtrack(self, n: int, path: List[str], left_used: int, right_used: int, result: List[str]):
        # 终止条件：当括号字符串的长度达到 2*n 时，是一个完整的解
        if len(path) == 2 * n:
            result.append("".join(path))
            return

        if left_used < n:
            # 1. 选择
            path.append('(')
            # 2. 递归
            self.backtrack(n, path, left_used + 1, right_used, result)
            # 3. 撤销
            path.pop()

        # 规则二：如果已使用的右括号数小于左括号数，就可以选择放一个右括号
        if right_used < left_used:
            # 1. 选择
            path.append(')')
            # 2. 递归
            self.backtrack(n, path, left_used, right_used + 1, result)
            # 3. 撤销
            path.pop()