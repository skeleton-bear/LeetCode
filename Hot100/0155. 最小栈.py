# 很重要,字节
import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = math.inf

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_val = val
        else:
            if val >= self.min_val:
                self.stack.append(val)
            else:
                # 存入包含最小值和原来的最小值信息的假值
                self.stack.append(2*val - self.min_val)
                self.min_val = val

    def pop(self) -> None:
        poped_val = self.stack.pop()

        # 如果弹出的值是假值,需要复原
        if poped_val < self.min_val:
            self.min_val = 2 * self.min_val - poped_val
        
        if not self.stack:
            self.min_val = math.inf
        
    def top(self) -> int:
        peeked_val = self.stack[-1]

        # 假值需要回复
        if peeked_val < self.min_val:
            return self.min_val
        else:
            return peeked_val
        
    def getMin(self) -> int:
        return self.min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()