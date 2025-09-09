# 很重要 腾讯二面手撕，略有变化：要求从链表尾部开始向前k个一组反转，最后不够k个的保持原顺序
# 字节校招面试题,团子一面面试题，撕出来没后续了，是不想要吗？

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            
            # --- 1. 检查剩余长度是否足够 k 个 ---
            # tail 指针向前走 k 步，检查是否会遇到 None
            tail = head
            for _ in range(k):
                # 如果中途 tail 变为 None，说明剩余节点不足 k 个
                if not tail:
                    return head # 直接返回，不做任何翻转
                tail = tail.next
            
            # --- 2. 翻转当前分组 (头 k 个节点) ---
            # 使用标准的迭代翻转链表逻辑
            prev = None
            curr = head
            # tail 在上面已经走到了第 k+1 个节点的位置
            # 所以我们只需要翻转到 tail 为止
            while curr != tail:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            
            # 循环结束后，prev 就是翻转后这一组的新头节点
            # head 变成了这一组的新尾节点
            
            # --- 3. 连接子问题 ---
            # 将新尾巴(head)的 next 指针，连接到对剩余部分递归调用的结果上
            # tail 此刻是下一组的头节点
            head.next = self.reverseKGroup(tail, k)
            
            # 4. 返回翻转后的新头节点
            return prev