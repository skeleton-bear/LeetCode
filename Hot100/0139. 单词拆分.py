class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        word_set = set(wordDict)

        # 1. dp[i] 表示 s 的前 i 个字符 s[0..i-1] 是否能被拆分
        dp = [False] * (n + 1)

        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                # 内层循环，j 代表切割点
                # 2. 应用状态转移方程
                # 如果 dp[j] 为 True (s[0..j-1]可拆分)
                # 并且 s[j..i-1] 这个子串在字典里
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]