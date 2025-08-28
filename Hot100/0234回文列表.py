# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 快慢指针接后半段反转链表
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 这时候slow刚刚到一半,将后半段反转
        prev = None
        cur = slow
        while cur:
            next_node =  cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        # 反转结束

        # 比较前后两段
        while prev:
            if head.val != prev.val:
                return False
            else:
                head = head.next
                prev = prev.next
        return True