# 很重要 美团
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -math.inf

        self.dfs(root)

        return self.max_sum
    
    def dfs(self,  node):
        if not node:
            return 0

        # 递归计算左右子节点能贡献的最大“单边”路径
        # 注意：如果子树贡献为负，我们宁愿不要，所以和0取max
        left_gain = max(self.dfs(node.left), 0)
        right_gain = max(self.dfs(node.right), 0)

        # 副作用：以当前节点为“拐点”的路径和，用它来更新全局最大值
        path_sum_at_this_node = node.val + left_gain + right_gain
        self.max_sum = max(self.max_sum, path_sum_at_this_node)

        # 返回值：返回以当前节点为起点的“单边”最大路径和，供上层使用
        return node.val + max(left_gain, right_gain)
        