class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        candidates.sort()
        self.backtrack(candidates, target, 0, path, result)
        return result

    
    def backtrack(self, candidates, target, start_index, path, result):
        if target == 0:
            result.append(path[:])
            return

        for i  in range(start_index, len(candidates)):
            if candidates[i] > target:
                break
            
            path.append(candidates[i])

            self.backtrack(candidates, target-candidates[i], i, path, result)

            path.pop()

        