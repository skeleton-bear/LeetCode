class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 回溯 +  回文判断工具
        result = []
        path = []
        self.backtrack(s, 0, path, result)
        return result
    
    def backtrack(self, s, start_index, path, result):
        # 终止条件：如果起始索引已经等于字符串长度，说明找到了一组分割方案
        if start_index >= len(s):
            result.append(path[:])
            return

        for i in range(start_index, len(s)):
            # 截取字符串
            substring = s[start_index : i + 1]

            # 判断是不是回文串
            if self.is_palindrome(substring):
                # 回溯三部曲
                path.append(substring)
                self.backtrack(s, i+1, path, result)
                path.pop()
    
    # 回文判断
    def is_palindrome(self, sub):
        return sub == sub[::-1]
        