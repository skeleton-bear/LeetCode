class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        reuslt = []
        path = []
        visited = [False] * len(nums)

        self.backtrack(nums, path,  visited , reuslt)
        return reuslt

    def backtrack(self, nums, path, visited, reuslt):
        if len(path) == len(nums):
            reuslt.append(path[:])
            return 

        # 遍历所有选择
        for i in range(len(nums)):
            if visited[i]:
                continue

            # 回溯三部曲
            path.append(nums[i])
            visited[i] = True

            self.backtrack(nums, path, visited, reuslt)

            # 撤回选择(回溯)
            visited[i] = False
            path.pop()


        