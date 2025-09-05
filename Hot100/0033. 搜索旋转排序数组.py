class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,  right = 0, len(nums) - 1

        while left <= right:
            mid = (left+right) // 2

            if nums[mid]  == target:
                return mid
            
            # 判断左半边是否有序
            if nums[left] <= nums[mid]:
                # 检查target是否在区间
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    # 去右半边找
                    left = mid + 1
            else:
                # 如果左半部分无序，那么右半部分 [mid...right] 必然有序
                # 判断 target 是否落在这个有序的区间内
                if nums[mid] < target <= nums[right]:
                    # 是，则在右半部分继续查找
                    left = mid + 1
                else:
                    # 不是，则只能去左半部分查找
                    right = mid - 1
        return -1