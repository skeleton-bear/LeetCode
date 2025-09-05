# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        p1, p2 = l1, l2

        # 只要p1或者p2,或者carry有一个不是0,就继续
        while p1 or p2 or carry:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            # 计算综合
            total_sum = val1 + val2 + carry
            # 计算新节点的数字和新的进位
            new_digit = total_sum % 10
            carry = total_sum // 10
            
            # 创建新节点并链接到结果链表
            current.next = ListNode(new_digit)
            
            # 移动所有指针
            current = current.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
                
        return dummy_head.next


        