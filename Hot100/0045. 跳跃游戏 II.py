class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0 # 当前这一跳能到达的最远边界
        farthest = 0 # 下一跳最远边界
        n = len(nums)

        for i in range(n -1):
            # 1. 在当前可达范围内，不断更新下一跳的最远边界
            farthest = max(farthest, i+nums[i])

            # 2. 到达当前跳跃的边界，必须进行下一次跳跃
            if i == current_end:
                jumps += 1
                # 更新下一次跳跃的边界
                current_end = farthest

                 # 优化：如果下一跳的边界已经覆盖了终点，可以提前结束
                if current_end >= n - 1:
                    break
        return jumps

