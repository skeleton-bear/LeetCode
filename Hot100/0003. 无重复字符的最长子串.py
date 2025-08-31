class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        char_set = set() # 哈希集合,存放当前窗口内的字符
        left = 0
        max_length = 0
        
        for right in range(n):
            # 查看s[right]是否再集合中
            while s[right] in char_set:
                char_set.remove(s[left]) # 在集合中就代表出现重复字符,移动左边
                left += 1

            char_set.add(s[right])

            max_length = max(max_length, (right - left +1))
        return max_length
        