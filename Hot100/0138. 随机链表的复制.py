class Node:
    """
    # Definition for a Node.
    """
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 哈希表，用于存储 {旧节点: 新节点} 的映射
        mapping = {}

        # --- 第一遍扫描：创建新节点并建立映射 ---
        current = head
        while current:
            # 创建新节点，值与旧节点相同
            new_node = Node(current.val)
            # 存入映射表
            mapping[current] = new_node
            current = current.next

        # --- 第二遍扫描：连接新节点的 next 和 random 指针 ---
        current = head
        while current:
            # 获取对应的新节点
            new_node = mapping[current]
            
            # 连接 next 指针
            # 如果 current.next 存在，就去 map 里找到对应的新 next 节点
            # 如果 current.next 是 None，map.get 会返回 None，正好是我们想要的
            new_node.next = mapping.get(current.next)
            
            # 连接 random 指针
            # 原理同上
            new_node.random = mapping.get(current.random)
            
            current = current.next
            
        # 返回新链表的头节点
        return mapping[head]