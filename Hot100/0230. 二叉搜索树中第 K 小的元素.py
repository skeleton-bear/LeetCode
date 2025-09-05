# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 二叉搜索树中序遍历后本身就是升序的
        result = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)

        return result[k-1]