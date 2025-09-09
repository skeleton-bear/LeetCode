class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        # 初始化
        # global_max: 最终要返回的全局最大值
        # max_here: 以当前元素结尾的最大乘积
        # min_here: 以当前元素结尾的最小乘积
        global_max = max_here = min_here = nums[0]
        for i in range(1, n):
            num = nums[i]
            # 如果当前数字是负数，最大值和最小值会互换
            if num < 0:
                max_here, min_here = min_here, max_here

            # 更新以当前元素结尾的最大和最小乘积
            # 选择1：从当前元素开始一个新的子数组 (num)
            # 选择2：将当前元素加入之前的子数组 (num * max_here)
            max_here = max(num, num * max_here)
            min_here = min(num, num * min_here)

            # 更新全局最大值
            global_max = max(global_max, max_here)

        return global_max