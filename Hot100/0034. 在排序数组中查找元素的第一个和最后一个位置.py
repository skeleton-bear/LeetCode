class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_b = self.find_left_boundary(nums, target)
        
        if left_b == len(nums) or nums[left_b] != target:
            return [-1,-1]
        
        right_b = self.find_right_boundary(nums, target)

        return [left_b, right_b]
    
    def find_left_boundary(self, nums, target):
        """查找第一个大于或等于 target 的索引"""
        left, right = 0, len(nums) - 1
        # 我们用 left_bound 来记录潜在的左边界，初始值为数组长度
        # 如果最终没找到，它会是 len(nums)，这是一个很好的哨兵值
        left_bound = len(nums)

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                # 找到了一个潜在的答案，继续向左收缩寻找更早的
                left_bound = mid
                right = mid - 1
            else: # nums[mid] < target
                # 目标在右侧
                left = mid + 1
        return left_bound
        
    def find_right_boundary(self, nums: List[int], target: int) -> int:
        """查找最后一个等于 target 的索引"""
        left, right = 0, len(nums) - 1
        # 我们用 right_bound 来记录潜在的右边界，初始值为-1
        right_bound = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                # 找到了一个潜在的答案，继续向右收缩寻找更晚的
                # 但只有当它确实等于target时，才更新
                if nums[mid] == target:
                    right_bound = mid
                left = mid + 1
            else: # nums[mid] > target
                # 目标在左侧
                right = mid - 1
        return right_bound
        