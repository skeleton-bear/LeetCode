class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 先对数组进行排序,固定第一个数后转化为寻找和为第一个数的相反数的两数之和问题
        # 然后使用双指针来解决那个“两数之和”子问题
        
        s_nums = sorted(nums)
        result = []

        for i in range(0, len(s_nums) - 2):
            if s_nums[i] > 0: # 后面的数字不可能和小于0
                break
            if i == 0:
                used = s_nums[i]
            if  used == s_nums[i] and i != 0:
                continue      
            used = s_nums[i]  # 记录之前处理过的数字避免重复处理
            
            # 双指针寻找相反数
            left = i + 1
            right = len(s_nums) - 1

            while left < right:
                if s_nums[left] + s_nums[right] + s_nums[i] < 0:
                    left += 1
                elif s_nums[left] + s_nums[right] + s_nums[i] > 0:
                    right -= 1
                else:
                    r = [s_nums[left] , s_nums[right] , s_nums[i]]
                    result.append(r)
                    
                    # 对剩下的两个元素去重
                    while left < right and s_nums[left] == s_nums[left + 1]:
                        left += 1
                    while left < right and s_nums[right] == s_nums[right - 1]:
                        right -= 1
                    
                    # 移动指针找下一组解
                    left += 1
                    right -= 1
        return result


