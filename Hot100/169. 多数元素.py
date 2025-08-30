class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        threshold = n // 2
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
            if count[num] > threshold:
                return num

        