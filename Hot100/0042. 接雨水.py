# 很重要 字节
from typing import List
# 解法一：动态规划 (O(n) 时间, O(n) 空间)
class Solution:
    def trap_dp(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
            
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
            
        right_max = [0] * n
        right_max[n-1] = height[n-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
            
        total_water = 0
        for i in range(n):
            water_level = min(left_max[i], right_max[i])
            total_water += water_level - height[i]
            
        return total_water

# 解法二：双指针 (O(n) 时间, O(1) 空间)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        total_water = 0
        
        while left < right:
            if height[left] < height[right]:
                # 处理左边
                if height[left] >= left_max:
                    # 当前柱子是新的左边最高点，它本身无法存水
                    left_max = height[left]
                else:
                    # 当前柱子比 left_max 矮，可以存水
                    total_water += left_max - height[left]
                left += 1
            else:
                # 处理右边
                if height[right] >= right_max:
                    # 当前柱子是新的右边最高点
                    right_max = height[right]
                else:
                    # 当前柱子比 right_max 矮，可以存水
                    total_water += right_max - height[right]
                right -= 1
                
        return total_water