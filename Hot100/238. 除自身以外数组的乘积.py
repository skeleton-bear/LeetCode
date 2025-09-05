class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 初始化answer数组,所有元素为1
        answer = [1] * n

        # 从左到右计算前缀积
        prefix_product = 1
        for i in range (n):
            answer[i] = prefix_product
            prefix_product *= nums[i]
        
        # 从右到左，计算后缀积并乘以之前的前缀积
        # range(n - 1, -1, -1) 表示从 n-1 倒序到 0
        suffix_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
        
        return answer
