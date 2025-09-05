# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre_p = dummy

        while pre_p.next and pre_p.next.next :
            temp = pre_p.next

            pre_p.next = pre_p.next.next

            temp.next = pre_p.next.next

            pre_p.next.next = temp
            pre_p = temp


        return dummy.next


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建虚拟头节点
        dummy = ListNode(0, head)
        # prev 是待交换的两个节点的前驱节点
        prev = dummy
        
        # 只要 prev 后面至少还有两个节点，就可以进行交换
        while prev.next and prev.next.next:
            # 1. 先用临时变量“抓住”这两个要交换的节点
            node1 = prev.next
            node2 = prev.next.next
            
            # 2. 开始执行指针交换的“四步曲”
            #    (画图理解会非常清晰)
            prev.next = node2
            node1.next = node2.next
            node2.next = node1
            
            # 3. 移动 prev 指针，为下一轮交换做准备
            prev = node1
            
        return dummy.next

