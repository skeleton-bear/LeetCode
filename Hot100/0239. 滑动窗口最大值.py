class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        q = deque()
        result = []

        for i in range(n):
            # a. 从队尾“清理”：移除所有比当前元素小的
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            # 从队尾“入队”：加入当前元素的索引
            q.append(i)

            # 从队首“检查”：移除已经滑出窗口的
            if q[0] == i - k:
                q.popleft()
            
            # 当窗口形成后，开始记录结果
            if i >= k - 1:
                result.append(nums[q[0]])
                
        return result


        