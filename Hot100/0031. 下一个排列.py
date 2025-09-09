# 很重要,字节
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        # 1. 从后向前找到第一个“升序”对 (nums[i] < nums[i+1])
        # i 是那个“小数位”的索引
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
            
        if i >= 0:
            # 2. 如果找到了这样的 i，再从后向前找到第一个比 nums[i] 大的数
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            
            # 3. 交换
            nums[i], nums[j] = nums[j], nums[i]
            
        # 4. 将 i 之后的部分反转 (或者，如果 i < 0，反转整个数组)
        # 无论是否找到 i，i+1 后面的部分都需要重排成最小序列
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

