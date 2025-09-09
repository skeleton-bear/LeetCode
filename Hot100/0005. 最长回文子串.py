class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n<2:
            return s
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]

        max_len = 1
        start = 0


        for i in range(n):
            dp[i][i] = True
        
        for j in range (1,n):
            for i in range(j):
                if s[i] == s[j]:
                # 如果子串长度小于等于2，只需要判断首尾字符
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        # 否则，依赖于内部子串的状态
                        dp[i][j] = dp[i+1][j-1]

                # 如果 dp[i][j] 是 True，我们更新最长回文串的记录
                if dp[i][j] and (j - i +1 > max_len):
                    max_len = j -i +1
                    start = i
        return s[start : start + max_len]