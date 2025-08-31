from ast import List


class Solution:
    def findAnagrams(self, s: str, p: str):
        if not s or not p:
            return []

        n = len(s)
        l = len(p)
        result = []
        for i in range(0,n):
            char_set = set(p) # 每次重置集合
            left = i
            right = i + l
            # 越界检测
            if right > (n-1):
                break
            wondows_set = set(s[left:right])
            for j in wondows_set:
                if j in char_set:
                    char_set.remove(j)
            if not char_set:  # 如果为空则代表滑动窗口内的元素和p一摸一样
                result.append(i)
        print(result)
        return result


solver = Solution()
solver.findAnagrams("abab","ab")