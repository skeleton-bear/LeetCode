# 很重要, 字节
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            # 使用 while 循环，确保交换过来的新数字也能被放到正确位置
            # 条件：
            # 1. nums[i] 是在 [1, n] 范围内的正数
            # 2. nums[i] 没有在它应该在的位置上 (nums[i] 应该在 nums[i]-1 的位置)
            while 1<= nums[i] <=n and nums[nums[i] - 1] != nums[i]:
                # 找到 nums[i] 应该去的目标索引
                targe_index = nums[i] -1
                nums[i], nums[targe_index] = nums[targe_index], nums[i]
        
        # --- 第二步：查找第一个不匹配的位置 ---
        for i in range(n):
            if nums[i] != i +1:
                return i+1
        
        return n+1
        