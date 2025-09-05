# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # 层序遍历的最后一个
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            # 遍历当前层数所有节点
            for i in range(level_size):
                node = queue.popleft()

                if i == level_size -1:
                    result.append(node.val)

                # 添加下一层的节点
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

        