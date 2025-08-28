'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]
'''

from ast import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 维护一前一后两个指针，将非0的数字和前面的0交换位置
        slow = 0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                # slow 位置往前移动，如果是0只有fast指针向前移动
                slow +=1