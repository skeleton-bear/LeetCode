# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 找出最大深度，然后计算直径，
# 会超时
class Solution:
# 将每个节点的左子树和右子树深度求出来，找出这个根节点最大的直径
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_diameter = 0
        nodes_to_visit = [root]
        
        while nodes_to_visit:
            node = nodes_to_visit.pop()
            
            left_depth = self.maxDepth(node.left)
            right_depth = self.maxDepth(node.right)
            
            current_diameter = left_depth + right_depth
            max_diameter = max(max_diameter, current_diameter)
            
            if node.left:
                nodes_to_visit.append(node.left)
            if node.right:
                nodes_to_visit.append(node.right)
                
        return max_diameter

    # 辅助函数：计算以 node 为根的子树的最大深度（节点数）
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))

# 解法2 直接使用递归寻找最大直径
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 这个实例变量，就相当于一个可以在所有递归调用中共享的“全局”变量
        self.max_diameter = 0
        
        # 我们只需要启动一次递归，它会像多米诺骨牌一样完成所有计算
        self.get_depth_and_update_diameter(root)
        
        # 当递归结束时，max_diameter 就已经被正确更新为最大值了
        return self.max_diameter

    def get_depth_and_update_diameter(self, node: Optional[TreeNode]) -> int:
        """
        这个函数返回以 node 为根的子树的深度，
        并且在过程中更新 self.max_diameter。
        """
        # 1. 递归出口
        if not node:
            return 0
        
        # 2. 向下深入，获取左右子树的深度信息 (这是后序遍历的 L 和 R)
        left_depth = self.get_depth_and_update_diameter(node.left)
        right_depth = self.get_depth_and_update_diameter(node.right)
        
        # 3. 处理当前节点 (这是后序遍历的 Root)
        #   [次要任务] 更新全局最大直径
        self.max_diameter = max(self.max_diameter, left_depth + right_depth)
        
        #   [主要任务] 将当前节点的深度返回给它的父节点
        return 1 + max(left_depth, right_depth)
    