class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按照其实位置排序
        intervals.sort(key = lambda a: a[0])

        # 初始化结果列表,放入第一个区间
        merged = [intervals[0]]

        # 从第二个区间开始遍历
        for i in range(1, len(intervals)):
            current_interval = intervals[i]

            # 结果列表中最后一个区间
            last_merged_interbal = merged[-1]

            # 判断是否重叠
            if current_interval[0] <= last_merged_interbal[1]:
                last_merged_interbal[1] = max(last_merged_interbal[1], current_interval[1])
            else:
                merged.append(current_interval)
        return merged
        