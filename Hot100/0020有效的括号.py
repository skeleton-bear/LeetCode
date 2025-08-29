class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 :
            return False
        
        stack = []
        # 使用哈希表来查找匹配的符号
        # key是左右括号,value是左括号
        brackets_map = {')':'(', ']':'[', '}': '{'}

        for char in s:
            # 如果是右括号
            if char in brackets_map:
                # 如果栈为空,或者栈中最后一个元素不是对应的左括号就是False
                if not stack or stack[-1] != brackets_map[char]:
                    return False
                # 匹配成功则弹出
                stack.pop()
            # 如果是左括号则直接入栈等待
            else:
                stack.append(char)
        # 循环结束后如果栈为空则都匹配到了,如果不为空则存在未匹配的括号
        return not stack
                
            
        