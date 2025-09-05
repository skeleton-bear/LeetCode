class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            '2':"abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        result = []
        path = []

        self.backtrack(digits, phone_map, 0, path,  result)
        return  result

    def backtrack(self, digits, phone_map, index, path, result):
        if index == len(digits):
            result.append("".join(path))
            return
        
        # 获取当前数字对应的选择列表
        current_digit = digits[index]
        letters = phone_map[current_digit]

        for letter in letters:
            path.append(letter)
            self.backtrack(digits, phone_map, index+1, path, result)
            path.pop()
        