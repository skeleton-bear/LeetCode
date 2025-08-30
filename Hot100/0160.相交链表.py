from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法1
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 哈希集合
        visited_node = set()
        # 遍历链表A，将所有节点存入集合
        pA = headA
        while pA:
            visited_node.add(pA)
            pA = pA.next
        
        # 遍历链表B，查看是否在集合里面
        pB = headB
        while pB:
            if pB in visited_node:
                return pB
            pB = pB.next
        
        return None

#解法2，双指针走路
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        while pA is not pB:
            # 如果 pA 走到头了，就把它指向 headB；否则，正常前进
            pA = pA.next if pA else headB
            
            # 如果 pB 走到头了，就把它指向 headA；否则，正常前进
            pB = pB.next if pB else headA
            
        # 当循环退出时，pA 和 pB 要么指向交点，要么同时为 None
        return pA