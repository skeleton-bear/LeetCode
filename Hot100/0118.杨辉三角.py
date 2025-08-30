class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        c = [[1] * (i+1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i): # 两边都是1 所以从1开始
                # 正上方的数字 + 左上方的数字 
                c[i][j] = c[i-1][j] + c[i-1][j-1]
        
        return c
        