class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.backtrack(nums, 0 ,path, result)
        return result

    def backtrack(self, nums, start_index, path, result):
        # 将当前路径加入result
        result.append(path[:])

        # 终止条件是隐式的,当start_index >= len(nums)时,下面的for循环不会进行

        for i in range(start_index, len(nums)):
            # 回溯三部曲
            path.append(nums[i])
            self.backtrack(nums, i+1, path, result)
            path.pop()

        