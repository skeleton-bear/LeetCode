# 很重要 快手
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        # 建立小顶堆
        min_heap = []
        
        # 1. 初始化：将 k 个链表的头节点加入堆中
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val,i, head))
        
        while min_heap:
            # a. 弹出当前所有头节点中的最小节点
            val, i, node = heapq.heappop(min_heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next


        