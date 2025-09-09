class MedianFinder:

    def __init__(self):
        # small_half 是大顶堆，存放较小的一半数字
        # Python 中用小顶堆存相反数来模拟
        self.small_half = []
        
        # large_half 是小顶堆，存放较大的一半数字
        self.large_half = []
        

    def addNum(self, num: int) -> None:
        # 1. 先将 num 加入 small_half (大顶堆)
        heapq.heappush(self.small_half, -num)
        
        # 2. 将 small_half 的最大值（堆顶）移动到 large_half
        #    以确保 small_half 的所有元素都小于等于 large_half
        largest_in_small = -heapq.heappop(self.small_half)
        heapq.heappush(self.large_half, largest_in_small)
        
        # 3. 检查并恢复平衡
        #    如果 large_half 的数量更多，则将其最小值移动到 small_half
        if len(self.large_half) > len(self.small_half):
            smallest_in_large = heapq.heappop(self.large_half)
            heapq.heappush(self.small_half, -smallest_in_large)
        

    def findMedian(self) -> float:
        # 如果总数是奇数，中位数在 small_half 的堆顶
        if len(self.small_half) > len(self.large_half):
            # 因为存的是相反数，所以要取反
            return float(-self.small_half[0])
        else:
            # 如果总数是偶数，中位数是两个堆顶的平均值
            return (-self.small_half[0] + self.large_half[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()