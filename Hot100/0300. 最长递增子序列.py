class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]：表示以 nums[i] 这个数结尾的最长递增子序列的长度。
        n = len(nums)

        if n == 0:
            return 0

        dp = [1]*n

        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)