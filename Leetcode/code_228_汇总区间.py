from typing import List


# 题目链接:https://leetcode.cn/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # 自己一开始写的 也是对的 不过写的狗屎一样也就我自己看得懂估计
        # n = len(nums)
        # if n == 1:
        #     return [str(nums[0])]
        # ans = []
        # start = 0
        # end = -1
        # for i in range(n):
        #     # 1.如果i位置和i-1位置值不是相差1且i位置和i+1位置值不是相差1 则i位置为独立区间
        #     # 2.如果i位置和i-1位置值不是相差1 则i位置为开始
        #     # 3.如果i位置和i+1位置值不是相差1 则i位置为结尾
        #     if i + 1 < n and nums[i + 1] != nums[i] + 1:
        #         end = i
        #     if i - 1 >= 0 and nums[i - 1] != nums[i] - 1:
        #         start = i
        #     if i == 0:
        #         start = i
        #         if nums[i] + 1 != nums[i + 1]:
        #             end = i
        #     if i == n - 1:
        #         end = i
        #         if nums[i] != nums[i - 1] + 1:
        #             start = i
        #     if end > start:
        #         ans.append(str(nums[start]) + '->' + str(nums[end]))
        #     elif end == start:
        #         ans.append(str(nums[start]))
        # return ans
        # 优化后
        n = len(nums)
        ans = []
        i = 0
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1
            end = nums[i]
            if end > start:
                ans.append(f"{start}->{end}")
            else:
                ans.append(f"{start}")
            i += 1
        return ans


print(Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]))
