# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root or root == p or root == q:
            return root
        
        # 向下递归,搜集左右子树情报
        left_found = self.lowestCommonAncestor(root.left, p, q)
        right_found = self.lowestCommonAncestor(root.right, p, q)

        # p 和 q 分别在左右子树中，当前 root 就是 LCA
        if left_found and right_found:
            return root
        
        # 情况二/三：p 和 q 都在左子树或右子树中，
        # 此时其中一个 found 是 None，另一个是找到的节点(或LCA)，
        # 我们返回那个不为 None 的即可。
        # 如果两边都找不到(都是None)，也自然会返回 None。
        return left_found if left_found else right_found
        