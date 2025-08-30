class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = sorted(list(set(nums)))
        count = 1
        longest = 0
        print(s)
        for i in range(0, len(s)-1):
            if s[i] +1 == s[i+1]:
                count += 1
            else:
                longest = max(longest, count)
                count = 1
        longest = max(longest, count)
        return longest

        