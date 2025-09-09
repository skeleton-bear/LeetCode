class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 1. 预处理：记录每个字符最后一次出现的位置
        last_occurrence = {char: i for i, char in enumerate(s)}

        reusult = []
        start,end = 0,0

        for i , char in enumerate(s):
            # 更新当前片段必须到达的最远边界
            end  = max(end, last_occurrence[char])

            # 如果当前索引 i 已经到达了最远边界 end
            # 说明找到了一个完整的片段，可以“切一刀”
            if i == end:
                partition_able = end - start + 1
                reusult.append(partition_able)

                start = i + 1
        return reusult
