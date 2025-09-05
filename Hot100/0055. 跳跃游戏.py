class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0

        # 遍历数组 i代表我们试图到达的位置
        for i in range(n):
            if i > max_reach:
                return False
            
            new_reach = i + nums[i]
            max_reach = max(max_reach, new_reach)

            if max_reach >= n-1:
                return True
        
        return True