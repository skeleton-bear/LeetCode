class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2,nums1


        m,n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) //2

            j = half_len - i

            max_left_1 = nums1[i - 1] if i != 0 else -math.inf
            min_right_1 = nums1[i] if i != m else math.inf

            max_left_2 = nums2[j - 1] if j != 0 else -math.inf
            min_right_2 = nums2[j] if j != n else math.inf

            # 检查是否是完美的分割
            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                # 找到了，根据总长度的奇偶性计算中位数
                if (m + n) % 2 == 0:
                    # 偶数
                    max_left = max(max_left_1, max_left_2)
                    min_right = min(min_right_1, min_right_2)
                    return (max_left + min_right) / 2.0
                else:
                    # 奇数
                    return float(max(max_left_1, max_left_2))
            elif max_left_1 > min_right_2:
                # i 太大了，需要向左收缩
                right = i - 1
            else: # max_left_2 > min_right_1
                # i 太小了，需要向右扩张
                left = i + 1  