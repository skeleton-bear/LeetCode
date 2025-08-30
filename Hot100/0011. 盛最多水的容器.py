class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 面积 = (right - left) * min(height[left], height[right])
        left = 0
        right = len(height) - 1

        maxA = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])

            # 移动比较短的板子
            if height[left] < height[right]:
                left += 1  
            else:
                right -= 1
            
            if area > maxA:
                maxA = area
        
        return maxA
        