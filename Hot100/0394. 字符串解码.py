# 很重要 PDD
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_number = 0
        current_string = ''

        for char in s:
            if char.isdigit():
                current_number = current_number*10 + int(char)
            
            elif char == "[":
                stack.append(current_string)
                stack.append(current_number)

                # 重置状态
                current_string = ''
                current_number = 0
            elif char == ']':
                # 遇到右括号，开始解码
                # 栈顶是数字，再下面是上一层的字符串
                repetition_count = stack.pop()
                last_string = stack.pop()
                # 核心解码步骤
                current_string = last_string + current_string * repetition_count
            else:
                current_string += char
        return current_string
        


        