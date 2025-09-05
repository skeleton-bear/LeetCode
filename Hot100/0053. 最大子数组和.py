import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, n):
            num = nums[i]

            current_sum = max(num, num+current_sum)
            max_sum = max(max_sum, current_sum)

        return max_sum
            
        