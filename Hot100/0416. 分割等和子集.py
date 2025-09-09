class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        dp = [False] *(target+1)
        dp[0] = True

        for num in nums:
            # 倒序遍历背包容量，确保每个物品只用一次
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]