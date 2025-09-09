class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needs = Counter(t)
        window = defaultdict(int)

        left, right = 0, 0
        valid = 0

        start = 0
        min_len = float('inf')

        while right < len(s):
            c = s[right]
            right += 1

            # 如果c是需要的字符就更新window和valid

            if c in needs:
                window[c] += 1
                if window[c] == needs[c]:
                    valid += 1
            # 当窗口有效的时候缩小窗口
            while valid == len(needs):
                # 更新最小字串记录
                if right - left < min_len:
                    start = left
                    min_len = right - left
                # d是将要移出窗口的字符
                d = s[left]
                left += 1

                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1
                    
                        

        # 如果 min_len 还是初始值，说明没有找到
        return "" if min_len == float('inf') else s[start : start + min_len] 
        