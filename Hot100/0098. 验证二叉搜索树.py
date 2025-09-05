# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev_val = -math.inf
        return self.inorder_traversal(root)
    def inorder_traversal(self, node):
        if not node:
            return True
        
        if not self.inorder_traversal(node.left):
            return False
        
        if node.val <= self.prev_val:
            return False
        self.prev_val = node.val

        # 检查右子树
        return self.inorder_traversal(node.right)
        
        

        