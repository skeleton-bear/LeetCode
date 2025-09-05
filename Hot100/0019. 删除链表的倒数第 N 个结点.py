# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 快慢指针法
        
        # 虚头节点处理删除头节点的情况
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # 快指针多走n步
        for _ in range(n+1):
            fast = fast.next
        
        # 快慢指针同时移动
        while fast:
            slow = slow.next
            fast = fast.next
        
        # 快指针进none了, 慢指针就在删除节点的前一位中
        slow.next = slow.next.next

        return dummy.next

        