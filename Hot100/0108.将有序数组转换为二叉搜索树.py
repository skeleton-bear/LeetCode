# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        找到数组的中间元素，将它作为当前这棵树的根节点。

        数组中，中间元素左边的部分，用来递归地构建根节点的左子树。

        数组中，中间元素右边的部分，用来递归地构建根节点的右子树。

        当数组部分为空时，说明没有节点了，返回 None。
        '''
        
        def build_tree(left: int, right:int) -> TreeNode | None:
            if left > right:
                return None
            
            # 找到中间索引
            mid = (left + right) // 2

            # 建立根节点
            root = TreeNode(nums[mid])

            # 使用递归构建左右子树
            root.left = build_tree(left, mid - 1)
            root.right = build_tree(mid+1, right)

            return root
        
        # 递归调用
        return build_tree(0, len(nums)-1)

        