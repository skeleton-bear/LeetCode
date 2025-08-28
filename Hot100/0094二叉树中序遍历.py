# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归解法
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # 递归解法
        def traverse(node):
            if not node:
                return
            
            # 1.访问左子树
            traverse(node.left)

            # 2.访问根节点
            result.append(node.val)

            # 3.访问右子树
            traverse(node.right)
        
        # 使用递归从根节点开始遍历
        traverse(root)
        return result

# 堆栈解法
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        
        while current or stack:
            # 步骤 A: 不断往左子树的深处走，沿途所有节点都压入栈
            while current:
                stack.append(current)
                current = current.left
            
            # 步骤 B: 已经到了最左边，从栈中弹出一个节点进行处理
            current = stack.pop()
            result.append(current.val)
            
            # 步骤 C: 转向该节点的右子树，准备对右子树进行中序遍历
            current = current.right
            
        return result
        
     
        