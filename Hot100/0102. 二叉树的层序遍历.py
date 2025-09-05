# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            # 层序节点,获取当前层的节点数量
            level_size = len(queue)

            current_level = []

            # 内层循环,处理当前层的所有节点
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # 将下一层的节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 4. 将当前层的结果加入最终结果列表
            result.append(current_level)
        
        return result
            
        