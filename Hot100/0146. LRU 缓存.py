class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # 哈希表作为cache
        self.cache = {}

        self.head = DLinkedNode()
        self.tail = DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node):
        """双向链表删除节点"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_head(self, node):
        """将一个节点放到双向链表的头部"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # 如果在cache里面
        node = self.cache[key]
        self._remove_node(node)
        self._add_to_head(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node  = self.cache[key]
            node.value = value
            # 移动到头部
            self._remove_node(node)
            self._add_to_head(node)
        
        else:
            # 检查容量
            if len(self.cache) == self.capacity:
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]
            
            # 创建新的节点
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)