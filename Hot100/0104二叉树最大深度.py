# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # 递归计算左子树最大深度
        left_depth = self.maxDepth(root.left)

        # 递归计算右子树最大深度
        right_depth =  self.maxDepth(root.right)

        # 当前树的深度
        return 1 + max(left_depth, right_depth)
        