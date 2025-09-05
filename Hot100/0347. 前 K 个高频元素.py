class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 计算频率
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        min_heap = []
        for num, freq in counts.items():
            heapq.heappush(min_heap, (freq,num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for freq,num in min_heap]
        