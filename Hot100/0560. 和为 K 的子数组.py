class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        我们想找的是 sum(nums[j...i]) == k。

        利用上面的公式，这就等价于 prefix_sum[i] - prefix_sum[j-1] == k。

        我们把这个公式变形一下，得到：prefix_sum[j-1] == prefix_sum[i] - k。
        '''
        count = 0
        current_sum = 0
        # 哈希表,存储{前缀和:出现次数}
        prefix_map = {0:1}

        for num in nums:
            current_sum += num

            # 计算我需要寻找的目标前缀和
            target = current_sum - k

            if target in prefix_map:
                count += prefix_map[target]

            # 将当前的前缀和存入哈希表，更新其出现次数
            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

        return count

