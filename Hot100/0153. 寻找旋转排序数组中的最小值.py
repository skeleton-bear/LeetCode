from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # 循环条件是 left < right，当它们相遇时，就找到了最小值
        while left < right:
            mid = (left + right) // 2
            
            # 情况一：mid 在右边的、值较小的、有序的部分
            if nums[mid] < nums[right]:
                # 最小值在 mid 的左边，或者 mid 本身就是最小值
                # 所以我们收缩右边界到 mid
                right = mid
            else: # nums[mid] > nums[right]
                # 情况二：mid 在左边的、值较大的、有序的部分
                # “断崖”和最小值必然在 mid 的右边
                # 所以我们收缩左边界到 mid + 1
                left = mid + 1
                
        # 循环结束时，left 和 right 相遇，指向同个元素，即为最小值
        return nums[left]

