# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 使用集合来判断
        cur = head
        visited_noed = set()

        while cur:
            if cur not in visited_noed:
                visited_noed.add(cur)
                cur = cur.next
            else:
                return True
        
        return False