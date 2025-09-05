# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         # --- 递归的终止条件 ---
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        prev = None
        slow, fast = head,head

        # 快慢指针的归并排序
        # 归并排序:找到中点分割,排序,最后合并,可以用递归来解决

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # 切断列表
        if prev:
            prev.next = None

        sorted_left = self.sortList(head)
        sorted_right  = self.sortList(slow)
    
        return self.mergeTwoLists(sorted_left, sorted_right)

    def mergeTwoLists(self, l1, l2):
        # 合并两个有序(但是其实都是单个的点)
        dummy = ListNode(0)
        current =dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 if l1 else l2

        return dummy.next