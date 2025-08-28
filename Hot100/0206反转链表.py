# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        current = head

        while current:
            # 临时保存下一个节点
            next_p = current.next

            # 反转当前指针
            current.next = p

            # 移动p和current指针
            p = current
            current = next_p
        
        return p
    

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 递归的出口
        if not head or not head.next:
            return head
        
        # 2. 递归调用，反转 head 后面的部分
        # 假设 reverseList(head.next) 已经将 head 后面的链表完美反转
        # 并返回了新的头节点 new_head (原始链表的尾节点)
        new_head = self.reverseList(head.next)
        
        # 3. 将当前 head 节点链接到反转后的链表末尾
        # head.next 此刻是反转后链表的尾节点
        head.next.next = head
        
        # 4. 断开 head 与原后续节点的链接，避免成环
        head.next = None
        
        # 5. 返回整个反转后链表的头节点
        return new_head