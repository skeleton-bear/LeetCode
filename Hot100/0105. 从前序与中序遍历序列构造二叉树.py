# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 建立索引哈希映射
        self.inorder_map = {val: i for i, val in enumerate(inorder)}
        self.preorder = preorder

        # 递归入口
        self.preorder_idx = 0

        # 初始调用
        return self.build(0, len(inorder) - 1)

    def build(self, inorder_left_idx, inorder_right_idx):
        # 终止的条件,中序遍历子序列为空
        if inorder_left_idx>inorder_right_idx:
            return None
        
        root_val = self.preorder[self.preorder_idx]
        root = TreeNode(root_val)
        
        # self.preorder_idx 向前进一步，为下一个子树的根节点做准备
        self.preorder_idx += 1
        
        # b. 在中序遍历映射中找到根节点的位置
        inorder_root_idx = self.inorder_map[root_val]
        
        # c. 递归构建左右子树
        #    注意：必须先构建左子树，再构建右子树，这和先序遍历的顺序一致
        root.left = self.build(inorder_left_idx, inorder_root_idx - 1)
        root.right = self.build(inorder_root_idx + 1, inorder_right_idx)
        return root
        