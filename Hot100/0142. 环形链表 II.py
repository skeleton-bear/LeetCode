# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 快慢指针判断环
        slow, fast = head, head
        meet_node = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meet_node = slow
                break
        
        if not meet_node:
            return None # 没有环
        
        # 寻找环的入口,一个指针从 head 出发，一个指针从相遇点出发

        finder = head
        while finder != meet_node:
            finder = finder.next
            meet_node = meet_node.next

        return finder
        