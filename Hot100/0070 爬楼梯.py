class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n

        # 超过2阶的方法其实F(N) = F(N-1) + F(N-2)
        a, b = 1, 2
        for _ in range(3, n + 1):
            # temp = F(i) = F(i-1) + F(i-2)
            temp = a + b
            # 更新 a 和 b，为下一次循环做准备
            a = b
            b = temp
        
        # 循环结束后，b 就代表了 F(n)
        return b