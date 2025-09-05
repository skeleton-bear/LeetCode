# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # 递归终止条件
        if not root:
            return 
        
        # 递归让左右子树拉平
        self.flatten(root.left)
        self.flatten(root.right)

        # 处理当前节点,让左右子树连接起来
        flattened_left = root.left
        flattened_right = root.right

        # 将根节点的左子树清空
        root.left = None

        # 如果左子链表不为空,则进行连接
        if flattened_left:
            root.right = flattened_left

            # 找到左子链表的末尾
            p = flattened_left
            while p.right:
                p = p.right
            
            # 将原来的右子链表接到左子链表的末尾
            p.right = flattened_right
        