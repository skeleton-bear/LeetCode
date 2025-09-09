from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # --- 第一步：快慢指针找到环中相遇点 ---
        slow, fast = 0, 0
        # 必须用 do-while 的逻辑，先走再判断
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        # --- 第二步：寻找环的入口 ---
        finder = 0
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]
            
        return finder

