# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, p: Optional[TreeNode], q : Optional[TreeNode]):
        # 如果左右节点都是空则对成
        if not p and not q:
            return True
        # 如果有一个是空，或者值相等则不对称,
        if (not p or not q ) or q.val != p.val:
            return False
        
        # 递归调用, 比较p的左子树和q的右子树
        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 遍历返回节点，如果不相等就抛出False
        if not root:
            return True # 如果根节点是空的判定为对称
        
        return self.isMirror(root.left, root.right)